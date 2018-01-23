from Webcrawler import *
from queue import Queue


class BFS(AbstractSearchExample.AbstractSearch):
    """See AbstractSearchExample for documentation help"""

    def __init__(self, fringe):
        super().__init__(fringe)

    def search(self, root, goal, maxDepth=0):
        currentDepth = 0
        visited = EmptyDictionary.EmptyDictionary()
        self.fringe.put((root, None))
        self.fringe.put(None)
        vertex = None
        count = 0

        while not self.fringe.empty():
            if currentDepth == maxDepth:
                return visited

            lastVertex, edge = vertex, self.fringe.get()
            if not edge:
                if not lastVertex:
                    return visited
                currentDepth += 1
                self.fringe.put(None)

            else:
                vertex, parent = edge
                if vertex not in visited:
                    visited[currentDepth].add((vertex, parent))
                    if vertex == goal:
                        return visited
                    print("Count:",count,"Depth:",currentDepth,"Visited:", [("%d:"%layer,len(visited[layer])) for layer in visited.keys()])
                    count += 1
                    links = WebNavigator.WebNavigator.getAbsoluteLinksFromPage(vertex)
                    if goal in links:
                        print("GOAL IN FRINGE")
                    for link in links:
                        self.fringe.put((link, vertex))
        return visited


if __name__ == "__main__":
    bfs = BFS(Queue())
    print("Depth Search:", bfs.search("https://www.google.com/", "https://plus.google.com/+google/posts/abBGhYQa4dK", 3))
