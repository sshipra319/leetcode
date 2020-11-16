class Multiset:
    
    def __init__(self):
        self.items = []

    def add(self, val):
        self.items.append(val)

    def remove(self, val):
        if val in self.items:
            self.items.remove(val)

    def __contains__(self, val):
        if val in self.items:
            return True
        return False
    
    def __len__(self):
        return len(self.items)