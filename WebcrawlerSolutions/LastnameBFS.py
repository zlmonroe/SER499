import WebcrawlerSolutions.AbstractSearchExample as ASE
from WebcrawlerSolutions.WebNavigator import WebNavigator
from WebcrawlerSolutions.EmptyDictionary import EmptyDictionary
from queue import Queue


class LastnameBFS(ASE.AbstractSearch):
    """See AbstractSearchExample for documentation help"""

    def __init__(self, fringe):
        super().__init__(fringe)

    def pointSearch(self, start, end):
        visited = []
        queue = Queue()
        queue.put((start, None))

        while not queue.empty():
            vertex, parent = queue.get()

            if vertex not in visited:
                visited.append((vertex, parent))
                if vertex == end:
                    return visited, queue

                links = WebNavigator.getAbsoluteLinksFromPage(vertex)
                for link in links:
                    queue.put((link, vertex))
        return visited

    def getPath(self, start):
        pass

    def depthSearch(self, start, maxDepth=-1):
        """

        :param start: The node for the search to begin at (in our case this is a URL)
        :param maxDepth: The (non-inclusive) depth for the search to end at. 0 is treated as the start node, and every
        node from there is 1, and so on. The default behavior should be unrestricted bfs when maxDepth < 0.
        :return: A dictionary of {depths: URLS} visited by the search
        :rtype EmptyDictionary
        """
        currentDepth = 0

        visited = EmptyDictionary()
        queue = self.fringe
        queue.put(start)
        queue.put(None)
        vertex = None
        count = 0

        while not queue.empty():
            if currentDepth == maxDepth:
                return visited

            lastVertex, vertex = vertex, queue.get()
            if not vertex:
                if not lastVertex:
                    return visited
                currentDepth += 1
                queue.put(None)

            elif vertex not in visited:
                count += 1
                if count % 10 == 0:
                    print("Depth:", currentDepth, "Count:", count, "Unexplored:", queue.qsize())
                visited[currentDepth].add(vertex)

                links = WebNavigator.getAbsoluteLinksFromPage(vertex)
                for link in links:
                    queue.put(link)
        return visited


if __name__ == "__main__":
    bfs = LastnameBFS(Queue())
    # print("Point Search:", bfs.pointSearch("https://www.google.com/", "https://www.google.com/services/"))
    print("Depth Search:",bfs.depthSearch("https://www.google.com/", 3))
