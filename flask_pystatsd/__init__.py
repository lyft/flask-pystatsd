import statsd
import os
from flask import current_app

try:
    # This is the suffix component of the metric name. It gets the UUID which is also the hostname.
    suffix = "heroku_" + os.popen('hostname').read().rstrip()
except:
    suffix = None

current_app.statsd = statsd.StatsClient(host=os.environ.get('STATSD_HOSTNAME', None),
    port=os.environ.get('STATSD_PORT', None),
    prefix=os.environ.get('CLUSTER_NAME', None),
    suffix=suffix)
