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

    def init_app(self, app):
        app.config.setdefault('host', '127.0.0.1')
        # This is the prefix component of the metric name. It depends on the config/environment variable CLUSTER_NAME which is set through 'heroku config:set'
        prefix = os.environ['CLUSTER_NAME']
        # This is the suffix component of the metric name. It gets the UUID which is also the hostname.
        suffix =  "heroku_" + os.popen('hostname').read().rstrip()
        # Where we send our stats to.
        host = os.environ['STATSD_HOSTNAME']
        port = 8127
        # Use the newstyle teardown_appcontext if it's available, otherwise fall back to the request context.
        #if hasattr(app, 'teardown_appcontext'):
        #    app.teardown_appcontext(self.teardown)
        #else:
        #    app.teardown_request(self.teardown)

    def connect(self):
        return statsd.StatsClient(host=host, port=port, prefix=prefix, suffix=suffix)

    #def teardown(self, exception):
    #   ctx = stack.top
        #if hasattr(ctx, 'sqlite3_db'):
        #    ctx.sqlite3_db.close()

    @property 
    def connection(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'statsd'):
                ctx.statsd = self.connect()
            return ctx.statsd

    def counter(self):
        connect.incr('VARIABLE')
    
    def timer(self):
        connect.timing('KEY', VALUE)


# This sets up the UDP connection to the statsd server.
        # catch exception try/catch in pystatsd, send udp packet to 127
        #before request hook. run on every request. 
        #global object or check to see if statsd is already integrated with flask extension
        # Use the newstyle teardown_appcontext if it's available,
        # otherwise fall back to the request context
        