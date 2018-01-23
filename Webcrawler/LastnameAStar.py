import Webcrawler.AbstractSearchExample as ASE
from queue import PriorityQueue


class LastnameDFS(ASE.AbstractSearch):
    """See AbstractSearchExample for documentation help"""

    def __init__(self, fringe):
        super().__init__(fringe)

    def search(self, root, goal, maxDepth):
        print("pointSearch")
        raise NotImplementedError


if __name__ == "__main__":
    aStar = LastnameDFS(PriorityQueue)
    aStar.search("www.google.com", "www.bing.com")