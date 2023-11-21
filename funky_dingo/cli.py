"""Console script for funky_dingo."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for funky_dingo."""
    click.echo("See click documentation")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
