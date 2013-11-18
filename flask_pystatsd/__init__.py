import statsd
import os
from flask import current_app

try:
    # This is the suffix component of the metric name. It gets the UUID which is also the hostname.
    suffix = "heroku_" + os.popen('hostname').read().rstrip()
except:
    suffix = None

class SendMetric(object):

    def __init__(self, app=None):
        self.app = app
        self.init_app(app)

    def init_app(self, app):
        app.before_request(self._before_request)

    def _before_request(self):
        self.statsd = statsd.StatsClient(host=os.environ.get('STATSD_HOSTNAME', None),
        port=os.environ.get('STATSD_PORT', None),
        prefix=os.environ.get('CLUSTER_NAME', None),
        suffix=suffix)
