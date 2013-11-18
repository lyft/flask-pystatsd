import statsd
import os
from flask import current_app

class SendMetric(object):

  def __init__(self, app=None):
    self.app = app
    
    
  # TODO: turn this into a before_request hook.
  def connect(self): 
    try:
      # The prefix component of the metric depends on the config/environment variable CLUSTER_NAME. 'heroku config:set'
      prefix = os.environ['CLUSTER_NAME']
    except:
      prefix = None
    
    try:
      # This is the suffix component of the metric name. It gets the UUID which is also the hostname.
      suffix =  "heroku_" + os.popen('hostname').read().rstrip()
    except:
      suffix = None
    

    return statsd.StatsClient(host=os.environ.get('STATSD_HOSTNAME', None),
                              port=os.environ.get('STATSD_PORT', None),
                              prefix=os.environ.get('CLUSTER_NAME', None),
                              suffix=suffix)
