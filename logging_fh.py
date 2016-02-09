"""
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
"""
import logging
import os


LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
LOGLEVEL = getattr(logging, LOGLEVEL)
LOGFORMAT = os.environ.get('LOGFORMAT', '[%(asctime)s] [%(process)s] [%(levelname).4s] [%(name)s] %(message)s')
LOGDATEFORMAT = os.environ.get('LOGDATEFORMAT', '%Y-%m-%d %H:%M:%S %z')


def setup():
    """Installs the logging configuration."""
    logging.basicConfig(level=LOGLEVEL, format=LOGFORMAT, datefmt=LOGDATEFORMAT)
