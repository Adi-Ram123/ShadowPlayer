from Constants import CREST_LIMIT

class Crests:
    def __init__(self):
        self.crest_list = []
    
    def updateCrest(self):
        for crest in self.crest_list:
            if not crest.isFaith:
                crest.update(-1)
        for crest in self.crest_list:
            if self.crest.count == 0:
                self.crest_list.remove(crest)
    
    def addCrest(self, crest):
        if len(self.crest_list) == CREST_LIMIT:
            return
        self.crest_list.append(crest)