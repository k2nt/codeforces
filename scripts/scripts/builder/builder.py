import os

from pathlib import Path

import typer

from scripts.builder.common import (
    filepath_option,
    dry_run_option,
)
from scripts.builder.langspecs import (
    CppLangSpecs,
    CppVersion,
)

import scripts.common.filepath as fp


cli = typer.Typer(name='build')


@cli.command()
def cpp(
        path: str = filepath_option,
        dry_run: bool = dry_run_option,
        cpp_version: CppVersion = typer.Option(
            default = CppLangSpecs.default_version.value,
            help = 'CPP version to compile.'
            ),
        exec_build_path: str = typer.Option(
            default = CppLangSpecs.exec_build_path,
            help='Path to build executable.'
            )
    ):
    """Build standalone CPP application."""
    path = fp.to_pwd_path(path)
        
    obj_file_path = (Path(exec_build_path) / (path.stem))
    print(f"g++ --std={cpp_version.value} {path} -o {obj_file_path}")
    
    if dry_run:
        exit(0)

    os.system(f"g++ --std={cpp_version.value} {path} -o {obj_file_path}")


@cli.command()
def java(path: str = filepath_option):
    """Build standalone Java application."""
    raise NotImplementedError()


if __name__ == '__main__':
    cli()
