from Webcrawler import *
from queue import PriorityQueue
import re

class Heuristic(AbstractSearchExample.AbstractSearch):
    """See AbstractSearchExample for documentation help"""

    def __init__(self, fringe):
        super().__init__(fringe)

    def search(self, root, goal, maxDepth=0):
        """
        This method should be an iterative search method
        that utilized a heuristic to manage the fringe.
        You will receive no points for a recursive definition.
        """
        currentDepth = 0
        count = 0
        visited = EmptyDictionary.EmptyDictionary(dict)
        self.fringe.put((root, None), 0)
        vertex = None

        while not self.fringe.empty():
            lastVertex, edge = vertex, self.fringe.get()
            vertex, parent = edge
            if vertex not in visited:
                visited[vertex] = {"parent": parent, "depth": currentDepth, "count": count}
                if vertex == goal:
                    return visited
                print("Count:", count, "Depth:", currentDepth, "Visited:", vertex)
                count += 1
                links = WebNavigator.WebNavigator.getAbsoluteLinksFromPage(vertex)
                if goal in links:
                    print("GOAL IN FRINGE")
                for link in links:
                    self.fringe.put((link, vertex), self.heuristic(link, goal))

    def heuristic(self, link, goal):
        def wordSplit(content):
            wordList = []
            for text in content:
                words = re.split('\s+', text)
                wordList += words
            return wordList

        content = set(wordSplit(WebNavigator.WebNavigator.getVisibleTextContent(link)))
        if self.goal != goal:
            self.goalContent = set(wordSplit(WebNavigator.WebNavigator.getVisibleTextContent(goal)))
            self.goal = goal
        matches = content.intersection(self.goalContent)
        print(len(matches), link, content, self.goalContent, end='\n')
        return len(matches)


if __name__ == "__main__":
    heuristic = Heuristic(PriorityQueue)
    heuristic.search("https://en.wikipedia.org/wiki/Dog", "https://en.wikipedia.org/wiki/Cat_senses")
