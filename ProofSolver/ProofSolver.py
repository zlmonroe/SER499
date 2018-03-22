import tkinter
import string


class ProofSolver(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)

        self.instructions = tkinter.Label(self, text="This solver uses proof by refutation to prove a statement holds"
                                                     " in a given knowledge base (KB). All input must be of the form"
                                                     "'a+b' or similarly 'a+(b+c)' all 'and' statements must be split"
                                                     "into separate phrases.",
                                          wraplength=500, justify=tkinter.LEFT)
        self.instructions.grid(row=0, column=0, columnspan=3)

        self.entryLabel = tkinter.Label(self, text="Knowledge Base")
        self.entryLabel.grid(row=1, column=0)

        self.proofEntries = []
        entry = tkinter.Entry(self)
        entry.grid(row=2, column=0)
        self.proofEntries.append(entry)

        self.updateEntries()

        self.proveLabel = tkinter.Label(self, text="Query")
        self.proveLabel.grid(row=1, column=1)
        self.prove = tkinter.Entry(self)
        self.prove.grid(row=2, column=1)

        self.resultLabel = tkinter.Label(self, text="Result")
        self.resultLabel.grid(row=1, column=2)
        self.resultButton = tkinter.Button(self, text="Solve", command=self.solveCallback)
        self.resultButton.grid(row=2, column=2)
        self.result = tkinter.Entry(self)
        self.result.config(state="disabled")
        self.result.grid(row=3, column=2)

    def updateEntries(self):
        """
        Adds or remove entry fields to the knowledge base
        :return: None
        """
        if self.proofEntries[-1].get():
            entry = tkinter.Entry(self)
            entry.grid(row=len(self.proofEntries) + 2, column=0)
            self.proofEntries.append(entry)
        elif len(self.proofEntries) > 1 and not self.proofEntries[-2].get():
            self.proofEntries.pop().grid_forget()
        self.after(100, self.updateEntries)

    def solveCallback(self):
        """
        Callback for the solve button. Calls ProofSolver#refutation
        :return: None
        """
        self.result.config(state="normal")
        self.result.delete(0, tkinter.END)
        self.result.insert(tkinter.END, self.refutation())
        self.result.config(state="disabled")

    def refutation(self):
        """
        Solved proof through refutation
        :return: string representing the solution to KB query
        :rtype: string
        """
        kb = [self.parsePhrase(box.get()) for box in self.proofEntries[:-1]]
        print("KB:", kb)
        alpha = self.inverse(self.parsePhrase(self.prove.get()))
        print("Alpha:", alpha)
        for part in alpha:
            kb.append(part)
        print("KB+A:", kb)

        def iteration(kb):
            for i in range(len(kb)):
                for j in range(len(kb)):
                    if set(kb[i]) & set(kb[j]):
                        kb.append(list(set(
                            [thing for thing in kb[i] if not any(self.isNegation(thing, thing2) for thing2 in kb[j])]) |
                                     set([thing for thing in kb[j] if
                                          not any(self.isNegation(thing, thing2) for thing2 in kb[i])])))

                        if not kb[-1]:
                            return True
                        return False

        while not iteration(kb):
            pass
        return ""

    def parsePhrase(self, phrase):
        """
        Creates a list with broken down form
        For example: a'+(b+c)' -> [a', b'c']
        :param phrase:
        :return:
        """
        phrase = phrase.replace(" ", "")

        invalid = [char not in ['(', ')', '+', "'"] + list(string.ascii_letters) for char in phrase]
        if any(invalid):
            raise SyntaxError("Invalid character '%s' at index: %d" %
                              (phrase[invalid.index(True)], invalid.index(True)))

        if len(phrase) == 1:
            return [phrase]

        prio = [0] * len(phrase)

        # identify parenthesis level
        level = 0
        for index in range(len(phrase)):
            if phrase[index] == ")":
                level -= 1
            prio[index] = level
            if phrase[index] == "(":
                level += 1

        # find top level '+'
        location = -1
        for index in range(len(phrase)):
            if phrase[index] == "+" and prio[index] == 0:
                if location == -1:
                    location = index
                else:
                    raise SyntaxError("Error at token +: found multiple top level operators at indexes [%d, %d] in %s"
                                      % (location, index, phrase))

        if location == -1:
            raise SyntaxError("Could not find top level operator or singleton in expression: '%s'" % phrase)

        return [self.simplifyNegation(phrase[:location]), self.simplifyNegation(phrase[location + 1:])]

    def inverse(self, parsed):
        """
        Determines the negation of a phrase
        :param parsed: list of strings representing facts (i.e. [a', bc'])
        :return: the negation of the list
        :rtype: list
        """
        parsed = ["".join(list(parsed))+"'"]

        return parsed

    def simplifyNegation(self, token):
        """
        Simplifies the negations inside of a single phrase
        :param phrase: string representing a boolean token of form a' or '(a+b)'
        :return: simplified string
        """
        # handle simple double negation
        token = token.replace("''", "")

        if "'" not in token:
            return token

        parenLevel = [0] * len(token)

        # identify parenthesis level
        level = 0
        for index in range(len(token)):
            if token[index] == ")":
                level -= 1
            parenLevel[index] = level
            if token[index] == "(":
                level += 1

        # find top level '+'
        location = -1
        for index in range(len(token)):
            if token[index] == "+" and parenLevel[index] == 0:
                if location == -1:
                    location = index
                else:
                    raise SyntaxError("Error at token +: found multiple top level operators at indexes [%d, %d] in %s"
                                      % (location, index, token))

        if location != -1:
            raise SyntaxError("Top level operator found in expression %s where single token was expected" %
                              (token))

        parenIndex = [index for index in range(len(parenLevel)) if parenLevel == 1]

        # find negated parenthesis
        negated = []
        for index in range(len(token), 1):
            if token[index] == "'" and token[index - 1] == ")":
                self.parsePhrase(token[token.index(parenLevel[index]):index - 1])

    def isNegation(self, a, b):
        return (len(a) > 1 and a[0:-1] == b) or (len(b) > 1 and b[0:-1] == a)


if __name__ == "__main__":
    root = ProofSolver()
    print(root.simplifyNegation("(a+b)''"))
    root.mainloop()
