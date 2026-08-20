"""DependencyCVE: Cross-checks dependency versions against a local advisory list."""

__version__ = "1.0.0"

from .core import run
from .cli import main

__all__ = ["main", "run", "__version__"]