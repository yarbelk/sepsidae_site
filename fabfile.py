from fabric.api import *
from fabric.contrib import files

env.roledefs.update({
    'staging': [''],
})

env.user = 'deploy'

repository_name = 'sepsidae_site'


@runs_once
def migrate():
    with cd('$HOME/{0}/src/{0}'.format(repository_name)):
        with prefix("export PATH=$HOME/.virtualenv/%s/bin:$PATH" % repository_name):
            with settings(shell='bash -i -c'):
                run('./manage.py syncdb -v0 --noinput --migrate '
                    '--settings=conf.settings.$SERVER_ENV')
                run('./manage.py rebuild_index -v0 --noinput '
                    '--settings=conf.settings.$SERVER_ENV')


@parallel
def up(branch):
    with cd('$HOME/{0}'.format(repository_name)):
        run('git checkout %s && git pull origin %s ' % (branch, branch),
            shell=False)

        with settings(shell='bash -i -c'):
            with settings(warn_only=True):
                # Will raise an error if there's no .pyc files.
                run('find -name *.pyc | xargs rm')
            with prefix("export PATH=$HOME/.virtualenv/%s/bin:$PATH" % repository_name):
                run('pip install -r requirements.txt', shell=False)
                with cd('src/%s' % repository_name):
                    run('./manage.py collectstatic -v0 --noinput '
                        '--settings=conf.settings.$SERVER_ENV')
    restart()


def start():
    run('supervisorctl start {0}'.format(repository_name))


def stop():
    run('supervisorctl stop {0}'.format(repository_name))


def restart():
    """This is not the same as running stop() and then start() which tells
    supervisord to restart the process. Instead it sends a HUP signal to the
    process which restarts it."""
    run('supervisorctl restart {0}'.format(repository_name))
