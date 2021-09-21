import traceback
from rdh import MessageContainer, create_parser, configure_redis, run_harness


def to_upper_case(msg_cont):
    """
    Processes the message container, turning the message into upper case.

    :param msg_cont: the message container to process
    :type msg_cont: MessageContainer
    """
    msg = msg_cont.message['data'].decode()
    msg = msg.upper()
    msg_cont.message = None
    msg_cont.params.redis.publish(msg_cont.params.channel_out, msg)


def main(args=None):
    """
    Parses the supplied arguments; if None, uses the command-line arguments supplied to the process.

    :param args: the arguments to parse
    :type args: list
    """
    parser = create_parser("String processing")
    parsed = parser.parse_args(args=args)
    params = configure_redis(parsed)
    run_harness(params, to_upper_case)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print(traceback.format_exc())
