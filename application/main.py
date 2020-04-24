from application.gamelist import gamelist
from application.game import game
import click


@click.group(invoke_without_command=True)
@click.pass_context
def log(ctx):
    if ctx.invoked_subcommand is None:
        gl = gamelist()
        click.echo(gl)
        # TODO: implement ui and main logic
    return


@log.command()
# @click.option('-t', '--title', default=None, type=str,
#               help="Add the specified game to gamelog")
@click.argument("title", type=str)
def add(title):
    '''Add the specified game to gamelog'''
    if title:
        gl = gamelist()
        gl += game(title)
        print("added game: " + title)
    else:
        with click.Context(add) as ctx:
            click.echo(add.get_help(ctx))


if __name__ == "__main__":
    print("GAMELOG ACTIVATED2")
