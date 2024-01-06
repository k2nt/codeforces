"""Filepath helpers."""
import os
from pathlib import Path


def pwd() -> Path:
    """Get current working directory.
    
    Returns:
        str: Current working directory
    """
    # Scripts run in the 'scripts' folder, while programs are compiled to their
    #   language folders. The '.parent' subscript is to resolve script paths to
    #   the working directory, i.e., 'scripts/...' -> '/...'
    return Path().resolve().parent


def to_pwd_path(path: str | Path) -> str:
    """Convert relative path with respect to current working directory.
    
    E.g. 'path' -> '$PWD'/'path'
    
    Arguments:
        path -- str: Relative file path
    
    Returns:
        str: Absolute file path
    """
    if os.path.isabs(path):
        return Path(path)
    
    return pwd() / path
