from Webcrawler import *
from queue import PriorityQueue


class LastnameHeuristic(ASE.AbstractSearch):
    """See AbstractSearchExample for documentation help"""

    def __init__(self, fringe):
        super().__init__(fringe)

    def search(self, root, goal, maxDepth=0):
        print("pointSearch")
        raise NotImplementedError


if __name__ == "__main__":
    aStar = LastnameHeuristic(PriorityQueue)
    aStar.search("https://www.google.com/", "https://store.google.com/category/phones")
