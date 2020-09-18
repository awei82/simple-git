import click

@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    #click.echo('Debug mode is %s' % ('on' if debug else 'off'))
    pass


@cli.command()
@click.argument('files', nargs=-1)
@click.option('--message', '-m')
def commit(files, message):
    click.echo(files)
    click.echo(message)

    if len(files) == 0:
        print('No files specified.')

    if not message or len(message.strip()) == 0:
        print('no message/empty message')

