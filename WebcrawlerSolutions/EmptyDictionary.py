class EmptyDictionary(dict):
    def __init__(self, default=set()):
        super().__init__(self)
        self.default = default

    def __getitem__(self, idx):
        self.setdefault(idx, self.default)
        return dict.__getitem__(self, idx)
