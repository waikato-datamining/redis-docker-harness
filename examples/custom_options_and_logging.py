import traceback
from rdh import Container, MessageContainer, create_parser, configure_redis, run_harness, log


def to_upper_case(msg_cont):
    """
    Processes the message container, turning the message into upper case.

    :param msg_cont: the message container to process
    :type msg_cont: MessageContainer
    """
    msg = msg_cont.message['data'].decode()
    # if in verbose mode, output the message
    if msg_cont.params.config.verbose:
        log(msg)
    msg = msg.upper()
    # if in verbose mode, output the processed string
    if msg_cont.params.config.verbose:
        log(msg)
    msg_cont.message = None
    msg_cont.params.redis.publish(msg_cont.params.channel_out, msg)


def main(args=None):
    """
    Parses the supplied arguments; if None, uses the command-line arguments supplied to the process.

    :param args: the arguments to parse
    :type args: list
    """
    parser = create_parser("String processing")
    parser.add_argument('--verbose', action='store_true',
                        dest='verbose', help='Whether to output some debugging information')
    parsed = parser.parse_args(args=args)
    # place custom options in container
    config = Container()
    config.verbose = parsed.verbose
    params = configure_redis(parsed, config=config)
    run_harness(params, to_upper_case)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print(traceback.format_exc())
