import sys
import argparse

from constants import DEFAULT_PYTHON_VERSION, DEFAULT_SERVER_NAME, DEFAULT_APP_NAME, \
    DEFAULT_NUM_WORKERS, DEFAULT_COMPOSE_DIR
from compose import build


def _parse_cmd_args(*args):
    parser = argparse.ArgumentParser()

    parser.add_argument("-pp",
                        "--project-path",
                        help="Path to the wsgi app project directory",
                        required=True)
    parser.add_argument("-wp",
                        "--wsgi-path",
                        help="Path to the WSGI module",
                        required=True)
    parser.add_argument("-sp",
                        "--static-path",
                        help="Path to the static directory of the project (should be inside it), default '</PROJECT/PATH>/static'",
                        required=False,
                        default=None)
    parser.add_argument("-mp",
                        "--media-path",
                        help="Path to the media directory of the project (should be inside it), default '</PROJECT/PATH>/media'",
                        required=False,
                        default=None)
    parser.add_argument("-rp",
                        "--requirements-path",
                        help="Path to the requirements file of wsgi app",
                        required=False,
                        default=None)
    parser.add_argument("-pyv",
                        "--python-version",
                        help="Python version of WSGI application (only numbers), default '3.6'",
                        required=False,
                        default=DEFAULT_PYTHON_VERSION)
    parser.add_argument("-sn",
                        "--server-name",
                        help="Server name (in Nginx conf), defaut 'localhost'",
                        required=False,
                        default=DEFAULT_SERVER_NAME)
    parser.add_argument("-an",
                        "--app-name",
                        help="WSGI application name, default 'wsgi_app'",
                        required=False,
                        default=DEFAULT_APP_NAME)
    parser.add_argument("-nw",
                        "--num-workers",
                        help="The number of workers for Gunicorn, default 3",
                        required=False,
                        default=DEFAULT_NUM_WORKERS)
    parser.add_argument("-bp",
                        "--builddir-path",
                        help="Path to the directory docker-compose to be run",
                        required=False,
                        default=DEFAULT_COMPOSE_DIR)


    cmd_args = parser.parse_args(args)
    return cmd_args.__dict__


def main():
    args_dict = _parse_cmd_args(*sys.argv[1:])
    build(**args_dict)


if __name__ == "__main__":
    main()
