import os
from invoke import task
from sys import version_info

ROOT_DIR = os.path.dirname(__file__)
PROJ = "src"
CHECK_INCLUDES = ("tasks.py", PROJ)
FLAKE8_CFG = os.path.join("dev", "flake8.cfg")


@task
def black(context):
    """Run black style checker."""
    if version_info >= (3, 6, 0):
        context.run("black --check %s" % (" ".join(CHECK_INCLUDES)))


@task
def flake8(context, rcfile=FLAKE8_CFG):
    """Run flake8 style checker."""
    context.run("flake8 --config=%s %s" % (rcfile, " ".join(CHECK_INCLUDES)))
