# -*- coding: utf-8 -*-
from datetime import datetime
from json_log_formatter import JSONFormatter as _JSONFormatter


class JSONFormatter(_JSONFormatter):

    def json_record(self, message, extra, record):
        """Prepares a JSON payload which will be logged.
        Override this method to change JSON log format.
        :param message: Log message, e.g., `logger.info(msg='Sign up')`.
        :param extra: Dictionary that was passed as `extra` param
            `logger.info('Sign up', extra={'referral_code': '52d6ce'})`.
        :param record: `LogRecord` we got from `JSONFormatter.format()`.
        :return: Dictionary which will be passed to JSON lib.
        """
        extra['message'] = message
        if 'log_time' not in extra:
            extra['log_time'] = datetime.utcnow()

        if 'log_name' not in extra:
            extra['log_name'] = record.name

        if record.exc_info:
            extra['exc_info'] = self.formatException(record.exc_info)

        return extra
