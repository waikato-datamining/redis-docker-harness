Changelog
=========

0.0.4 (2023-07-25)
------------------

- added the `redis_timeout` parameter to the argparse options to make the pubsub thread `sleep_time` parameter
  configurable from the command-line (the default is now 0.01 instead of 0.001 to avoid high CPU load)
- the `create_parser` method can now specify the default values for: host, port, db, channel_in, channel_out, sleep_time


0.0.3 (2023-07-10)
------------------

- fixed password support when accessing environment variable


0.0.2 (2023-07-07)
------------------

- added support for supplying a password to use for the Redis connection (--password/--password_env)


0.0.1 (2021-09-22)
------------------

- initial release
