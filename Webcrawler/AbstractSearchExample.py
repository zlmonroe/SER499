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
    def search(self, root, goal, maxDepth=0):
        """
        Defines point to point, depth limited search

        :param maxDepth: the depth the search should end at
        :param goal: the target of the search
        :param root: Starting node of the search
        """
        pass


if __name__ == "__main__":
    pass
