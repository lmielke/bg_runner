# configs.py
# this is an example api for runner

from runner import settings as sts
from runner.runner import ResourceManager


def configs_getter(*args, verbose: int = 0, **kwargs):
    inst = ResourceManager(*args, verbose=verbose, **kwargs)
    inst(*args, verbose=verbose, **kwargs)  # Calls ensure() via __call__()
    if verbose:
        print(inst.cfg._config_summary(*args, verbose=verbose, **kwargs))
    return inst


def main(*args, **kwargs):
    """
    All entry points must contain a main getter like main(*args, **kwargs)
    """
    configs_getter(*args, **kwargs)
