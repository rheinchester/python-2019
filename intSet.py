class inteSet(object):
    def __init__(self):
        self.vals = []
        
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
            
    def isMember(self, e):
            return e in self.vals
                
    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise (ValueError(str(e) + ' not found'))
    def show(self):
        print(self.vals)
            
            
    
