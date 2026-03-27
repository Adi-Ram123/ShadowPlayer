class Crests:
    def __init__(self):
        self.LIMIT = 5
        self.crest_list = []
    
    def updateCrest(self):
        to_remove = []
        for crest in self.crest_list:
            if not crest.isFaith:
                crest.update(-1)
                if crest.count == 0:
                    to_remove.append(crest)
        for crest in to_remove:
            self.crest_list.remove(crest)
    
    def addCrest(self, crest):
        if len(self.crest_list) == self.LIMIT:
            return
        self.crest_list.append(crest)