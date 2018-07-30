# list example

cities = ["indore", "mumbai", "jodhpur", "schaumburg", "cicinnati"]
print("Print Cities list")
print(cities)
print("Print City 0 and city 3")
print(cities[0], cities[3])
print("Change city 3")
cities[3] = "hoffman estates"
print(cities[0], cities[3])
print("Print Cities list")
print(cities)
cities.sort()
print("Print sorted cities list")
print(cities)
cities.append("chicago")
print(cities)
print(len(cities))
print("Print cities list after removing 4 th city")
cities.pop(3)
print(cities)
print(len(cities))
