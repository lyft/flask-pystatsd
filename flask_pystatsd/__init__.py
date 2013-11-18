import statsd
import os
from flask import current_app

try:
    # This is the suffix component of the metric name. It gets the UUID which is also the hostname.
    suffix = "heroku_" + os.popen('hostname').read().rstrip()
except:
    suffix = None

def setup_app(app):
    app.statsd = statsd.StatsClient(host=os.environ.get('STATSD_HOSTNAME', '127.0.0.1'),
    port=(os.environ.get('STATSD_PORT', '8125'),
    prefix=os.environ.get('CLUSTER_NAME', 'None'),
    suffix=suffix)
