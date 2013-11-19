import statsd
import os

try:
    # This is the suffix component of the metric name. It gets the UUID which is also the hostname.
    suffix = "heroku_" + os.popen('hostname').read().strip()
except:
    suffix = None

def setup_app(app):
    port=os.environ.get('STATSD_PORT', None)
    if port:
        # convert to an integer given that StatsClient expects an integer.
        port=int(port)
    app.statsd = statsd.StatsClient(
        host=os.environ.get('STATSD_HOST', None),
        port=port,
        prefix=os.environ.get('STATSD_PREFIX', None),
        suffix=suffix)
