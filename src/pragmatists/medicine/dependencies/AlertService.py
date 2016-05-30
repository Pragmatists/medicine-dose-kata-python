from abc import ABCMeta, abstractmethod


class AlertServices:
    def __init__(self):
        pass

    __metaclass__ = ABCMeta

    @abstractmethod
    def notifyDoctor(self):
        pass
