from Webcrawler import *
from queue import Queue


class LastnameBFS(ASE.AbstractSearch):
    """See AbstractSearchExample for documentation help"""

    def __init__(self, fringe):
        super().__init__(fringe)

    def search(self, root, goal, maxDepth=0):
        print("pointSearch")
        raise NotImplementedError


if __name__ == "__main__":
    bfs = LastnameBFS(Queue)
    bfs.search("https://www.google.com/", "https://store.google.com/category/phones")
