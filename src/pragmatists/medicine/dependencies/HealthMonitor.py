from abc import ABCMeta, abstractmethod


class HealthMonitor:
    def __init__(self):
        pass

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_systolic_blood_pressure(self):
        pass
