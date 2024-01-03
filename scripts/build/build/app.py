from typer import Typer


from build.common import filepath_option


cli = Typer(name='build')


@cli.command()
def cpp(path: str = filepath_option):
    """Build standalone CPP application."""
    print('cpp')


def java8(path: str = filepath_option):
    """Build standalone Java 8 application."""
    raise NotImplementedError()


if __name__ == '__main__':
    cli()
