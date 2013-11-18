import statsd
import os
from flask import current_app

# Boilerplate Extension code from http://flask.pocoo.org/docs/extensiondev/
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

class SendMetric(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

       def connect(self):
        # use try & catch
        # This is the prefix component of the metric name. It depends on the config/environment variable CLUSTER_NAME which is set through 'heroku config:set'
        prefix = 'no_cluster_name_defined'
        prefix = os.environ['CLUSTER_NAME']
        # This is the suffix component of the metric name. It gets the UUID which is also the hostname.
        suffix = 'no_hostname_defined'
        suffix =  "heroku_" + os.popen('hostname').read().rstrip()
        # Where we send our stats to.
        #host = '127.0.0.1'
        host = os.environ['STATSD_HOSTNAME']
        port = 8127
        
        return statsd.StatsClient(host=host, port=port, prefix=prefix, suffix=suffix)