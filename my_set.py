class MySet():
    def __init__(self):
        self.items = []
  
    def add(self, object):
        """Adds an object to the set.
        If the object is already in the set, nothing happens.
        """
        if object not in self.items:
            self.items.append(object)
    
    def remove(self, object):
        self.items.remove(object)