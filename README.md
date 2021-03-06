logging_fh
===

Logging for humans.

Usage
-----

Installation is easy. Just import logging_fh and run
`logging_fh.setup()`. Use the logging module like usual.

```python
# Setup logging with logging_fh.
>>> import logging_fh
>>> logging_fh.setup()
# Use the logging module like usual.
>>> import logging
>>> logger = logging.getLogger(__name__)
>>> logger.info('woot!')
[2016-02-09 15:41:30 +0000] [20500] [INFO] [__main__] woot!
```

Configuration
-------------

You can change your log format by setting the following
environment variables.


| Environment Variable | Description                                                                                                 |
|----------------------|-------------------------------------------------------------------------------------------------------------|
| LOGLEVEL             | The logging level to use. Can be set to the following:   * DEBUG  * INFO  * WARNING  * ERROR  * CRITICAL    |
| LOGFORMAT            | Logging format to use.  Defaults to: `[%(asctime)s] [%(process)s] [%(levelname).4s] [%(name)s] %(message)s` |
| LOGDATEFORMAT        | Date format to use.  Defaults to: `%Y-%m-%d %H:%M:%S %z`                                                    |
