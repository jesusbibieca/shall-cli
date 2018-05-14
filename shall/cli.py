import click
import subprocess


@click.command()
@click.option('--install', '-i', is_flag=True, help='This will install supported shall packages.')
@click.argument('package', required=True)
def main(package, install):
    """shall is intented to simplify the installation process of the different packages in linux."""
    if install:
        # click.echo('Installing {}.'.format(package))

        cmd = 'curl http://localhost:8080/{}'.format(package)
        args = cmd.split()
        process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        click.echo(stdout)
        # click.echo(stderr)
    else:
        click.echo('Shall package {} have the following command:\nCMD'.format(package))


