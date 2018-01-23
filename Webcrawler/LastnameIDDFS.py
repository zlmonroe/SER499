import Webcrawler.AbstractSearchExample as ASE
from queue import LifoQueue


class LastnameDFS(ASE.AbstractSearch):
    """See AbstractSearchExample for documentation help"""

    def __init__(self, fringe):
        super().__init__(fringe)

    def search(self, root, goal):
        print("pointSearch")
        raise NotImplementedError

if __name__ == "__main__":
    iddfs = LastnameDFS(LifoQueue)
    iddfs.search("www.google.com", "www.bing.com")
