
class SysSetting(object):
    def __init__(self, freq=1.2e9):
        self.freq = freq


class Laser(object):
    def __init__(self, t='offchip', sys=SysSetting()):
        self.area = 0
        self.power = 0
        self.latency = 0

class MRR(object):
    def __init__(self, sys=SysSetting()):
        self.area = 0
        self.power = 0
        self.reconf_time = 0
        self.tuning_time = 0
        self.trans_bits = 8	# this is for analog communication only. may change later


class PD(object):
    def __init__(self, sys=SysSetting()):
        self.area = 0
        self.power = 0
        self.latency = 5.8e-12	# 5.8ps -> data from CrossLight [34]

class Node(object):
    def __init__(self, sys=SysSetting()):
        self.area = 0
        self.power = 0
        


