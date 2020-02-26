from Planet import Planet
class Planetary(object):
    
    
    def __init__(self,planets):
        self.planets = planets


    
    def menu(self):
        for i in range(8):
            print(str(i+1) + ": " + self.planets[i].getname())
        st = input("Enter a number ")
        if(int(st) < 9 ):
            print("Name: " + self.planets[int(st)-1].getname())
            print("Orbital Period: " + str(self.planets[int(st)-1].getobp()) + " Days")
            print("Surface Gravity: " + str(self.planets[int(st)-1].getgrav()) + " m/s^2")
            print("Mass: " + str(self.planets[int(st)-1].getmass()) + " x 10^25")
        t = input("Would you like to look at another planet? y/n ")
        if(t == "y"):
            self.menu()
        
