from Webcrawler import *
from queue import LifoQueue
import re

class DFS(AbstractSearchExample.AbstractSearch):
    """See AbstractSearchExample for documentation help"""

    def __init__(self, fringe):
        super().__init__(fringe)

    def search(self, root, goal, maxDepth=0):
        # 1. While BFS isn't exactly the first choice for implementing a webcrawler,
        # DFS is almost never used. What advantages does BFS have over DFS? Why
        # would DFS be impractical?
        #
        # 2. List the searches in order of which search would be best to use for this
        # type of problem. Be sure to explain your though process on each as this is
        # what will be graded, not your order. There are reasons for MOST orderings.
        return re.sub("\n *","\n","""
        Student's Responses:
        **********Answer Below*****************
        1.
        
        2.
        ***************************************
        """)


if __name__ == "__main__":
    dfs = DFS(LifoQueue)
    print(dfs.search("", ""))