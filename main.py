from Planet import Planet
from Planetary import Planetary

planets = [Planet("Mercury",87.9691,3.7,.033011),Planet("Venus",224.701,8.87,.48675),
               Planet("Earth",365,9.8,.597237),Planet("Mars",686.971 ,3.72076 ,.064171),
               Planet("Jupiter",4332.59 ,24.79,189.82),Planet("Saturn",10759.22,10.44,56.834),
               Planet("Uranus",30688.5,8.69,8.6810),Planet("Neptune",60182 ,11.15,10.2413)]

solar = Planetary(planets)

solar.menu()
