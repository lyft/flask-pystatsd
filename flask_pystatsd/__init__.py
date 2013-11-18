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
      suffix = 'no_suffix_hostname_defined'
    
    try:
      # Where we send our stats
      host = os.environ['STATSD_HOSTNAME']
    except:
      host = 'statsd-development-iad.lyft.net'
        
    port = 8127
      
    return statsd.StatsClient(host=host, port=port, prefix=prefix, suffix=suffix)
