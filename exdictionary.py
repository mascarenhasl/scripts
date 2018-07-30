# dictionary example

cities = {"ind": "indore", "bom": "mumbai", "jod": "jodhpur", "sch": "schaumburg", "cin": "cicinnati"}
print("Print Cities list")
print(cities)
print("Print City ")
city1 ="ind"
city2 = "jod"
print (city1)
print(city2)
print(cities[city1], cities[city2])
print("Change city cin")
cities["cin"] = "cincy"
print(cities)
print("Number of cities")
cities.update({"chi": "chicago"})
print(cities)
print(len(cities))
cities.pop(city1)
print(cities)
print(len(cities))
