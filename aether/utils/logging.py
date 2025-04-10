"""
Logging utilities for the Æther project
"""

import logging
import os
import sys
from typing import Any, Optional

# Custom log level for verbose output
VERBOSE = 15
logging.addLevelName(VERBOSE, "VERBOSE")


class AetherLogger(logging.Logger):
    """
    Custom logger for the Æther project with additional log levels.
    """

    def verbose(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """
        Log a message with VERBOSE level.

        Args:
          msg: The message to log.
          *args: Positional arguments for the log message.
          **kwargs: Keyword arguments for the log message.
        """

        if self.isEnabledFor(VERBOSE):
            self.log(VERBOSE, msg, args, **kwargs)


# Register the custom logger
logging.setLoggerClass(AetherLogger)


def setup_logger(
    name: str = "aether",
    level: int = logging.INFO,
    log_file: Optional[str] = None,
    console: bool = True,
    format_string: Optional[str] = None,
) -> logging.Logger:
    """Set up a logger with the given configuration.

    Args:
        name: The name of the logger.
        level: The log level.
        log_file: Path to the log file (if None, no file logging is set up).
        console: Whether to log to the console.
        format_string: Custom format string for the logger.

    Returns:
        Configured logger instance.
    """

    logger = logging.getLogger(name)
    logger.propagate = False

    if logger.handlers:
        logger.handlers.clear()

    logger.setLevel(level)
    if format_string is None:
        format_string = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    formatter = logging.Formatter(format_string)

    if log_file:
        log_dir = os.path.dirname(os.path.abspath(log_file))
        os.makedirs(log_dir, exist_ok=True)

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    if console:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger


def get_logger(name: str = "aether") -> logging.Logger:
    """
    Get an existing logger or create a new one with default settings

    Args:
        name: The name of the logger.

    Returns:
        Configured logger instance.
    """

    logger = logging.getLogger(name)

    if not logger.handlers:
        console_handler = logging.StreamHandler(sys.stdout)

        format_string = "[%(levelname)s] %(name)s: %(message)s"
        formatter = logging.Formatter(format_string)

        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        logger.setLevel(logging.INFO)

    return logger
