import statsd
import os
from flask import current_app

class statsd(object):

    def __init__(self, app=None):
        self.app = app

    def init_app(self, app):
        try:
            # This is the suffix component of the metric name. It gets the UUID which is also the hostname.
            suffix = "heroku_" + os.popen('hostname').read().rstrip()
        except:
            suffix = None

        app.before_request(self._before_request)

    def _before_request(self):
        return statsd.StatsClient(host=os.environ.get('STATSD_HOSTNAME', None),
        port=os.environ.get('STATSD_PORT', None),
        prefix=os.environ.get('CLUSTER_NAME', None),
        suffix=suffix)
