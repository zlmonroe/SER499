from abc import ABC, abstractmethod, ABCMeta


class AbstractSearch(ABC):
    __metaclass__ = ABCMeta

    def __init__(self, fringe):
        """
        :param fringe: defines how the fringe elements should be handled
        :type fringe: Queue, PriorityQueue, LifoQueue
        """
        super().__init__()
        self.fringe = fringe

    @abstractmethod
    def pointSearch(self, start, end):
        """
        Defines the path search method (i.e. point to point)

        :param start: Starting node"""
        pass

    @abstractmethod
    def depthSearch(self, start, depth=0):
        """
        Defines the depth search method (search for websites but give up at a certain depth). Default
        is depth = 0 which will not end at any depth.
        """
        pass


if __name__ == "__main__":
    pass
