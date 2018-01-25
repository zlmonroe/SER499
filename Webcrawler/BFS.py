from Webcrawler import *
from queue import Queue
import json


class BFS(AbstractSearchExample.AbstractSearch):
    """See AbstractSearchExample for documentation help"""

    def __init__(self, fringe):
        super().__init__(fringe)

    def search(self, root, goal, maxDepth=0):
        """
        This method should be an ITERATIVE definition of BFS.
        You will receive no points for a recursive implementation.
        """
        currentDepth = 0
        visited = EmptyDictionary.EmptyDictionary(dict)
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
                    visited[vertex] = {"parent":parent, "depth":currentDepth, "count":count}
                    if vertex == goal:
                        return visited
                    print("Count:",count,"Depth:",currentDepth,"Visited:",vertex)
                    count += 1
                    links = WebNavigator.WebNavigator.getAbsoluteLinksFromPage(vertex)
                    if goal in links:
                        print("GOAL IN FRINGE")
                    for link in links:
                        self.fringe.put((link, vertex))
        return visited


if __name__ == "__main__":
    bfs = BFS(Queue())
    with open("dfsSearch.txt", "w+") as file:
        print("Depth Search:", json.dumps(bfs.search("https://www.google.com/", "https://drive.google.com/?tab=wo", 3), indent=1), file=file)
        # "https://plus.google.com/+google/posts/abBGhYQa4dK"
