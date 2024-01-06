import typer


filepath_option = typer.Option(
    None,
    help="Path to file.",
    exists=True
    )
dry_run_option = typer.Option(
    False,
    help="Executes without making changes.",
)
