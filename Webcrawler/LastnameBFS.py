import Webcrawler.AbstractSearchExample as ASE
from queue import Queue


class LastnameDFS(ASE.AbstractSearch):
    """See AbstractSearchExample for documentation help"""

    def __init__(self, fringe):
        super().__init__(fringe)

    def search(self, root, goal, maxDepth):
        print("pointSearch")
        raise NotImplementedError

if __name__ == "__main__":
    bfs = LastnameDFS(Queue)
    bfs.search("https://www.google.com/", "https://store.google.com/category/phones")
