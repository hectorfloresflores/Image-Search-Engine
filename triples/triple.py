

class Triple:

    def __init__(self,sub,pred,obj):
        super().__init__
        self.subject = sub
        self.predicate = pred
        self.object = obj

    def getSubject(self):
        return self.subject
    
    def getPredicate(self):
        return self.predicate
    
    def getObject(self):
        return self.object


