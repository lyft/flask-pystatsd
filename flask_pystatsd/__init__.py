import statsd
import os
from flask import current_app

try:
    # This is the suffix component of the metric name. It gets the UUID which is also the hostname.
    suffix = "heroku_" + os.popen('hostname').read().rstrip()
except:
    suffix = None

# We want the application to error and not start if these variables are not set.
def setup_app(app):
    app.statsd = statsd.StatsClient(host=os.environ['STATSD_HOSTNAME'],
    port=int(os.environ['STATSD_PORT']),
    prefix=os.environ['CLUSTER_NAME'],
    suffix=suffix)
