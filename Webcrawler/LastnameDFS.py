import Webcrawler.AbstractSearchExample as ASE
from queue import LifoQueue


class LastnameDFS(ASE.AbstractSearch):
    """See AbstractSearchExample for documentation help"""

    def __init__(self, fringe):
        super().__init__(fringe)

    def search(self, root, goal):
        # While BFS isn't exactly the first choice for implementing a webcrawler,
        # DFS is almost never used. What advantages does BFS have over DFS? Why
        # would DFS be impractical?
        print("""
        Students Response:
        """)


if __name__ == "__main__":
    dfs = LastnameDFS(LifoQueue)
    dfs.search("", "")
