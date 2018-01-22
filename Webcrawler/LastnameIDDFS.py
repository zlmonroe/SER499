import Webcrawler.AbstractSearchExample as ASE
from queue import LifoQueue


class LastnameDFS(ASE.AbstractSearch):
    """See AbstractSearchExample for documentation help"""

    def __init__(self, fringe):
        super().__init__(fringe)

    def pointSearch(self, start, end):
        print("pointSearch")
        raise NotImplementedError

    def depthSearch(self, start, depth=0):
        print("depthSearch")
        raise NotImplementedError


if __name__ == "__main__":
    iddfs = LastnameDFS(LifoQueue)
    iddfs.pointSearch("www.google.com", "www.bing.com")
    iddfs.depthSearch("www.google.com")
