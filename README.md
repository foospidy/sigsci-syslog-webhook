# sigsci-syslog-webhook
A cloud function to forward Signal Sciences webhook messages to syslog

## Instructions

1. Edit the variables `SYSLOG_HOST` and `SYSLOG_PORT` to point to your syslog server.
2. Deploy the function to IBM Cloud Functions.
3. In Signal Sciences (Configure > Integrations), create a generic webook using the cloud function's public url.

Note: This function should work fine on any other cloud function platform that supports Python, e.g. AWS Lambda.

## Deploy Function

`bx wsk action update sigsci-syslog-webhook --memory 128 --kind python:3 --web true __main__.py`
