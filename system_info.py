import platform
import cpuinfo
import socket
import os
import psutil
import gpustat

class SystemInfo:
    def __init__(self):
        self.system = platform.system()
        self.node = platform.node()
        self.release = platform.release()
        self.version = platform.version()
        self.username = os.getlogin()
        self.hostname = socket.gethostname()
        self.ip_address = socket.gethostbyname(self.hostname)
        self.cpu_name = cpuinfo.get_cpu_info()['brand_raw']
        self.cpu_freq = psutil.cpu_freq().current
        self.cpu_max_freq = psutil.cpu_freq().max
        self.cpu_cores = psutil.cpu_count()
        self.cpu_usage = psutil.cpu_percent()
        self.gpus = gpustat.new_query().jsonify()
        self.disk_usage = self.get_disk_usage()
        self.mem_total = psutil.virtual_memory().total
        self.mem_available = psutil.virtual_memory().available
        self.mem_used = psutil.virtual_memory().used
        self.mem_percent = psutil.virtual_memory().percent
        
    def get_disk_usage(self):
        disk_usage = []
        for partition in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                disk_usage.append({
                    'name': partition.mountpoint,
                    'usage': {
                        'total': usage.total,
                        'used': usage.used,
                        'free': usage.free,
                        'percent': usage.percent
                    }
                })
            except PermissionError:
                pass
        return disk_usage

    def to_json(self):
      print(self.gpus)
      return {
          'system': self.system,
          'node': self.node,
          'release': self.release,
          'version': self.version,
          'username': self.username,
          'hostname': self.hostname,
          'ip_address': self.ip_address,
          'cpu_name': self.cpu_name,
          'cpu_freq': self.cpu_freq,
          'cpu_max_freq': self.cpu_max_freq,
          'cpu_cores': self.cpu_cores,
          'cpu_usage': self.cpu_usage,
          'gpus': self.gpus,
          'disk_usage': self.disk_usage,
          'mem_total': self.mem_total,
          'mem_available': self.mem_available,
          'mem_used': self.mem_used,
          'mem_percent': self.mem_percent
      }
