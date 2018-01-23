from Webcrawler import *
from queue import LifoQueue


class IDDFS(AbstractSearchExample.AbstractSearch):
    """See AbstractSearchExample for documentation help"""

    def __init__(self, fringe):
        super().__init__(fringe)

    def search(self, root, goal, maxDepth=0):
        def _dfsLimited(start, limit):
            self.fringe.push(start, [start])
            visited = set()

            while not self.fringe.isEmpty():
                state, path = self.fringe.pop()

                if state not in visited:
                    visited.add(state)
                    if end == state:
                        return path
                    for newState in WebNavigator.WebNavigator.getAbsoluteLinksFromPage(state):
                        self.fringe.push((newState, [newState] + path))
            return []

        for limit in range(0, maxDepth):
            result = _dfsLimited()
            if result is None:
                continue
            return result
        return None


if __name__ == "__main__":
    iddfs = IDDFS(LifoQueue)
    iddfs.search("https://www.google.com/", "https://store.google.com/category/phones")