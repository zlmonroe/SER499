import re
import json

def StudentSolutions():
    # 1. While BFS isn't exactly the first choice for implementing a webcrawler,
    # DFS is almost never used. What advantages does BFS have over DFS? Why
    # would DFS be impractical?
    #
    # 2. List the searches in order of which search would be best to use for this
    # type of problem. Be sure to explain your though process on each as this is
    # what will be graded, not your order. There are reasons for MOST orderings.
    #
    # 3. Why would IDDFS be a bad search algorithm to use for this problem? List
    # at least 3 disadvantages to using IDDFS for this project. What sort of
    # webcrawler problem(s) would IDDFS be more suited for?
    studentSolutions = {
        1: """\
        Answer for problem 1 (delete this)
        """,
        2: """\
        Answer for problem 2 (delete this)
        """,
        3: """\
        Answer for problem 3 (delete this)
        """
    }
    for key in studentSolutions.keys():
        studentSolutions[key] = re.sub(r"  +", "", studentSolutions[key]).rstrip("\n")

    return studentSolutions


if __name__ == "__main__":
    solutions = StudentSolutions()
    for problemNumber in solutions.keys():
        print("%d:\n"%problemNumber, solutions[problemNumber], sep='')