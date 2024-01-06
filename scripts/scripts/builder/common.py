import typer


filepath_option = typer.Option(
    None,
    help="Path to file.",
    exists=True
    )
