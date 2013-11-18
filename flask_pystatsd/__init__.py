import statsd
import os
from flask import current_app

class SendMetric(object):

  def __init__(self, app=None):
    self.app = app

  def connect(self): 
    try:
      # The prefix component of the metric depends on the config/environment variable CLUSTER_NAME. 'heroku config:set'
      prefix = os.environ['CLUSTER_NAME']
    except:
      prefix = 'no_cluster_name_defined'
    
    try:
      # This is the suffix component of the metric name. It gets the UUID which is also the hostname.
      suffix =  "heroku_" + os.popen('hostname').read().rstrip()
    except:
      suffix = 'no_hostname_defined'
    
    # Where we send our stats to.
    #host = '127.0.0.1'
    host = os.environ['STATSD_HOSTNAME']
    port = 8127
      
    return statsd.StatsClient(host=host, port=port, prefix=prefix, suffix=suffix)
