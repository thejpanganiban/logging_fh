logging_fh
===

Logging for humans.

Usage
-----

Installation is easy. Just import logging_fh and run
`logging_fh.setup()`.

```python
import logging_fh
logging_fh.setup()
```

Configuration
-------------

You can change your log format by setting the following
environment variables.

|               |                                                                                                             |
|---------------|-------------------------------------------------------------------------------------------------------------|
| LOGLEVEL      | The logging level to use. Can be set to the following:  - DEBUG - INFO - WARNING - ERROR - CRITICAL         |
| LOGFORMAT     | Logging format to use.  Defaults to: `[%(asctime)s] [%(process)s] [%(levelname).4s] [%(name)s] %(message)s` |
| LOGDATEFORMAT | Date format to use.  Defaults to: `%Y-%m-%d %H:%M:%S %z`                                                    |
