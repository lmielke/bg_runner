"""
pararses runner arguments and keyword arguments
args are provided by a function call to mk_args()

RUN like:
import runner.arguments
kwargs.updeate(arguments.mk_args().__dict__)
"""

import argparse
from typing import Dict


def mk_args():
    parser = argparse.ArgumentParser(description="run: python -m runner <api> [options]")

    # Positional API name
    parser.add_argument(
        "api",
        metavar="api",
        help="API to run, e.g., 'run', 'info', 'stop', see runner.apis"
    )

    # Optional kwargs
    parser.add_argument(
        "-i", "--infos",
        nargs="+",
        type=str,
        default=None,
        help="List of infos to be retrieved, default: all"
    )

    parser.add_argument(
        "-v", "--verbose",
        nargs="?",
        const=1,
        type=int,
        default=0,
        help="0: silent, 1: user, 2: debug"
    )

    parser.add_argument(
        "-y", "--yes",
        nargs="?",
        const=1,
        type=bool,
        default=None,
        help="Run without confirmation (unused)"
    )

    parser.add_argument(
        "--cmd",
        choices=["start", "stop", "info"],
        default="start",
        help="Command for background runner (default: start)"
    )

    parser.add_argument(
        "-m", "--module",
        required=False,
        help="Target Python module to run (e.g., altered.api_server)"
    )

    parser.add_argument(
        "--no-gui",
        action="store_true",
        help="Disable GUI components like tray icon or message boxes"
    )

    parser.add_argument(
        "--hard",
        action="store_true",
        default = None,
        help="Print actions without executing them"
    )

    parser.add_argument(
        "--id",
        type=str,
        help="Manually specify instance ID"
    )

    return parser.parse_args()



def get_required_flags(parser: argparse.ArgumentParser) -> Dict[str, bool]:
    """
    Extracts the 'required' flag for each argument from an argparse.ArgumentParser object.

    Args:
        parser (argparse.ArgumentParser): The parser to extract required flags from.

    Returns:
        Dict[str, bool]: A dictionary with argument names as keys and their 'required' status as values.
    """
    required_flags = {}
    for action in parser._actions:
        if isinstance(action, argparse._StoreAction):
            # For positional arguments, the 'required' attribute is not explicitly set,
            # but they are required by default.
            is_required = (
                getattr(action, "required", True)
                if action.option_strings == []
                else action.required
            )
            # Option strings is a list of option strings (e.g., '-f', '--foo').
            for option_string in action.option_strings:
                required_flags[option_string] = is_required
            if not action.option_strings:  # For positional arguments
                required_flags[action.dest] = is_required
    return required_flags


if __name__ == "__main__":
    parser = mk_args()
    required_flags = get_required_flags(parser)
    print(required_flags)
