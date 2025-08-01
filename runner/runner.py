"""
runner.py
This is an example module for a properly formatted Python bgrtype project.
"""

import os
import sys
import re
import inspect
import logging
from datetime import datetime as dt
from typing import List
from tabulate import tabulate
from colorama import Fore, Style

LOG = logging.getLogger(__name__)


class ConfigHandler:
    """
    Collects runtime paths, environment info, and project metadata
    for use by the background runner system.
    """

    def __init__(self, *args, verbose: int = 0, **kwargs) -> None:
        self.verbose = verbose
        self.run_id = dt.now().strftime("%Y-%m-%d_%H%M%S")

        # Project paths
        self.cwd = os.getcwd()
        self.pg_root = os.path.dirname(os.path.abspath(__file__))
        self.pg_name = (
                        __package__
                        or inspect.getmodule(self).__package__
                        or os.path.basename(self.pg_root)
        )

        # Executable info
        self.exe_path = os.path.abspath(sys.executable)
        self.exe_name = os.path.basename(self.exe_path)
        preferred_exe = os.path.join(os.path.dirname(self.exe_path), "pythonw.exe")
        self.exe_preferred = preferred_exe if os.path.exists(preferred_exe) else self.exe_path

        # Resource + log directories
        self.resources_dir = os.path.join(self.pg_root, "resources")
        self.log_base_dir = os.path.join(self.resources_dir, "logs")
        self.log_dir = os.path.join(self.log_base_dir, self.pg_name)
        self.config_dir = os.path.join(self.pg_root, "config")
        self.tmp_dir = os.path.join(self.resources_dir, "tmp")

        # Runtime files
        self.pid_file = os.path.join(self.log_dir, f"{self.pg_name}.pid")
        self.icon_path = os.path.join(self.resources_dir, "images", f"{self.pg_name}.png")

        # User
        self.user = os.getenv("USERNAME") or os.getenv("USER") or "unknown"

        if self.verbose >= 2:
            print(self._config_summary())

    def _config_summary(self, *args, **kwargs) -> str:
        rows = [
            (attr, str(value))
            for attr, value in self.__dict__.items()
            if not attr.startswith("_")
        ]
        return tabulate(rows, headers=["Config Key", "Value"], tablefmt="fancy_grid")

    def __str__(self, *args, **kwargs) -> str:
        return f"ConfigHandler: self.pg_name = '{self.pg_name}'"


class ResourceManager:
    """
    Manages and validates all path-based config entries from ConfigHandler.
    Supports dry-run creation of missing directories. Callable via __call__().
    """

    opt_exts = {'.pid', '.log', '.tmp'}
    opt_keys = {'icon_path'}

    def __init__(self, *args, **kwargs):
        self.cfg = ConfigHandler(*args, **kwargs)
        self.missing_dirs = {}
        self.missing_files = {}

    def __call__(self, *args, **kwargs):
        return self.ensure(*args, **kwargs)

    def create_missing(self, *args, verbose: bool = False, **kwargs ) -> None:
        for name, path_str in self.missing_dirs.items():
            msg = f"{Fore.RED}hard Creating: {Fore.RESET}{path_str}"
            os.makedirs(path_str, exist_ok=True)
            LOG.info(msg)
            if verbose:
                print(msg)

    def find_missings(self, *args, verbose: int = 0, **kwargs) -> dict:
        self.missing_dirs, self.missing_files = {}, {}
        abs_path_regex = re.compile(rf"^[A-Z]:{re.escape(os.sep)}", re.IGNORECASE)
        for name, path_str in vars(self.cfg).items():
            if isinstance(path_str, str) and abs_path_regex.match(path_str):
                if not os.path.exists(path_str):
                    if re.compile(r"\.[a-zA-Z0-9]{1,5}$").search(path_str):
                        self.missing_files[name] = path_str
                    else:
                        self.missing_dirs[name] = path_str
        if self.missing_dirs and verbose:
            print(
                f"\n{Fore.YELLOW}Missing directories found: "
                f"{tabulate(self.missing_dirs.items(), headers=['Name', 'Path'])}"
                f"{Fore.RESET}"
            )
        if self.missing_files and verbose:
            print(
                f"\n{Style.DIM}{Fore.WHITE}Missing files found: "
                f"{tabulate(self.missing_files.items(), headers=['Name', 'Path'])}"
                f"{Style.RESET_ALL}"
            )

    def ensure(self, *args, hard: bool = None, verbose: int = 0, **kwargs) -> None:
        self.find_missings(*args, verbose=verbose, **kwargs)
        if self.missing_dirs:
            if hard:
                self.create_missing(*args, verbose=verbose, **kwargs)
            else:
                print(f"{Fore.GREEN}Test run: not creating dirs.{Fore.RESET}")
        return self.missing_dirs, self.missing_files
