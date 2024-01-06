import os

import typer

from scripts.builder.common import filepath_option
from scripts.builder.langspecs import (
    CppLangSpecs,
    CppVersion,
)


cli = typer.Typer(name='build')


@cli.command()
def cpp(
        path: str = filepath_option,
        cpp_version: int = typer.Option(
            default = CppVersion.CPP17,
            help = 'CPP version to compile.'
            ),
        exec_build_path: str = typer.Option(
            default = CppLangSpecs.exec_build_path,
            help='Path to build executable.'
            )
    ):
    """Build standalone CPP application."""
    if cpp_version not in CppLangSpecs.accepted_versions:
        print(f"CPP version not supported. Supported versions are {str(CppVersion)}")
        exit(1)
        
    os.system(f"g++ --std={CppVersion.CPP17} {path} -o {exec_build_path}")


@cli.command()
def java(path: str = filepath_option):
    """Build standalone Java application."""
    raise NotImplementedError()


if __name__ == '__main__':
    cli()
