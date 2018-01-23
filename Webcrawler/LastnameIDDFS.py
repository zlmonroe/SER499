import Webcrawler.AbstractSearchExample as ASE
from queue import LifoQueue


class LastnameIDDFS(ASE.AbstractSearch):
    """See AbstractSearchExample for documentation help"""

    def __init__(self, fringe):
        super().__init__(fringe)

    def search(self, root, goal, maxDepth=0):
        print("pointSearch")
        raise NotImplementedError

if __name__ == "__main__":
    iddfs = LastnameIDDFS(LifoQueue)
    iddfs.search("https://www.google.com/", "https://store.google.com/category/phones")
