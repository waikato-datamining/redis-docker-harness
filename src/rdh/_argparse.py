import argparse
import os


def create_parser(description, prog=None, prefix="", host="localhost", port=6379, db=0,
                  channel_in=None, channel_out=None, sleep_time=0.01):
    """
    Configures a command-line parser with parameters for redis.

    :param description: the description that the parser outputs on the help screen
    :type description: str
    :param prog: the program name, when using entry_points, None to ignore
    :type prog: str
    :param prefix: the prefix to use for the command-line arguments
    :type prefix: str
    :param host: the default redis host
    :type host: str
    :param port: the default redis port
    :type port: int
    :param db: the default redis database
    :type db: int
    :param channel_in: the default incoming redis channel
    :type channel_in: str
    :param channel_out: the default outgoing redis channel
    :type channel_out: str
    :param sleep_time: the default pubsub timeout parameter
    :type sleep_time: float
    :return: the configured parser
    :rtype: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(description=description,
                                     prog=prog,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--%shost' % prefix, metavar='HOST', required=(host is None), default=host, type=str,
                        dest='redis_host', help='The redis server to connect to')
    parser.add_argument('--%sport' % prefix, metavar='PORT', required=(port is None), default=port, type=int,
                        dest='redis_port', help='The port the redis server is listening on')
    parser.add_argument('--%spassword' % prefix, metavar='PASSWORD', required=False, default=None, type=str,
                        dest='redis_password', help='The password to use for connecting')
    parser.add_argument('--%spassword_env' % prefix, metavar='PASSWORD', required=False, default=None, type=str,
                        dest='redis_password_env', help='The environment variable to obtain the password from to use for connecting')
    parser.add_argument('--%sdb' % prefix, metavar='DB', required=(db is None), default=db, type=int,
                        dest='redis_db', help='The redis database to use')
    parser.add_argument('--%sin' % prefix, metavar='CHANNEL', required=(channel_in is None), default=channel_in, type=str,
                        dest='redis_in', help='The redis channel to receive the data from')
    parser.add_argument('--%sout' % prefix, metavar='CHANNEL', required=(channel_out is None), default=channel_out, type=str,
                        dest='redis_out', help='The redis channel to publish the processed data on')
    parser.add_argument('--%stimeout' % prefix, metavar='NUM', required=(sleep_time is None), default=sleep_time, type=float,
                        dest='redis_timeout', help='The timeout to use for the pubsub thread sleep_time parameter.')
    return parser


def has_password(ns):
    """
    Checks the namespace whether a password has been supplied either directly or via environment variable.
    Direct password takes precedence over environment variable.

    :param ns: the namespace to check
    :return: True if a password has been supplied
    :rtype: bool
    """
    if hasattr(ns, "redis_password"):
        if ns.redis_password is not None:
            return True

    if hasattr(ns, "redis_password_env"):
        if ns.redis_password_env is not None:
            if os.getenv(ns.redis_password_env) is not None:
                return True

    return False


def get_password(ns):
    """
    Returns the password from the namespace (supplied either directly or via environment variable).
    Direct password takes precedence over environment variable.

    :param ns: the namespace to use
    :return: the password if one has been supplied, otherwise None
    :rtype: str
    """
    if hasattr(ns, "redis_password"):
        if ns.redis_password is not None:
            return ns.redis_password

    if hasattr(ns, "redis_password_env"):
        if ns.redis_password_env is not None:
            if os.getenv(ns.redis_password_env) is not None:
                return os.getenv(ns.redis_password_env)

    return None
