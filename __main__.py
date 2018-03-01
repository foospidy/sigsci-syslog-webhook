"""
A cloud function to forward Signal Sciences webhook messages to syslog
"""
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#

import sys
import logging
import logging.handlers

SYSLOG_HOST = "<syslog_host>"
SYSLOG_PORT = 514

def main(dict):
    syslogger = logging.getLogger('MySysLogger')
    syslogger.setLevel(logging.INFO)
    handler = logging.handlers.SysLogHandler(address = (SYSLOG_HOST, SYSLOG_PORT))
    syslogger.addHandler(handler)
    syslogger.info(dict['message'])

    return { 'message': 'Sent to syslog!' }
