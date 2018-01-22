from queue import LifoQueue
import WebcrawlerSolutions.AbstractSearchExample as ASE
from WebcrawlerSolutions.WebNavigator import WebNavigator
from WebcrawlerSolutions.EmptyDictionary import EmptyDictionary


class LastnameDFS(ASE.AbstractSearch):
    """See AbstractSearchExample for documentation help"""

    def __init__(self, fringe):
        super().__init__(fringe)

    def depthSearch(self, start, end, maxDepth=0):
        def _dfsLimited(start, limit):
            self.fringe.push(start, [start])
            visited = set()

            while not self.fringe.isEmpty():
                state, path = self.fringe.pop()

                if state not in visited:
                    visited.add(state)
                    if end == state:
                        return path
                    for newState in WebNavigator.getAbsoluteLinksFromPage(state):
                        self.fringe.push((newState, [newState] + path))
            return []

        for limit in range(0, maxDepth):
            result = _dfsLimited()
            if result is None:
                continue
            return result
        return None


if __name__ == "__main__":
    iddfs = LastnameDFS(LifoQueue())
    # iddfs.pointSearch("www.google.com", "www.bing.com")
    print(iddfs.depthSearch("https://www.google.com/", 2))
