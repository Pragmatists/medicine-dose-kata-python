from abc import ABCMeta, abstractmethod


class MedicinePump:
    def __init__(self):
        pass

    __metaclass__ = ABCMeta

    @abstractmethod
    def dose(self, medicine):
        pass

    @abstractmethod
    def getTimeSinceLastDoseInMinutes(self, medicine):
        pass