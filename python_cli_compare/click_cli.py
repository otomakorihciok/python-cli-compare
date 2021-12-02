import click


@click.group()
def cli():
    pass


@cli.command("to_num")
@click.argument("num", type=int)
@click.option("--base", default=10)
def to_num(num, base):
    click.echo(base * num)
