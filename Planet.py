class Planet(object):


    def __init__(self,name,obp,grav,mass):
        self.name = name
        self.obp = obp
        self.grav = grav
        self.mass = mass

    def getobp(self):
        return self.obp
    def getname(self):
        return self.name
    def getgrav(self):
        return self.grav
    def getmass(self):
        return self.mass
    
