bicycles = ['Trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
# -1 index returns the last element in a list
print(bicycles[-1])
print(bicycles[-2])
message = f'My first bicyle was {bicycles[0].title()}'
print(message)

# changing, adding, removing elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(1, 'ducati')
print(motorcycles)
del motorcycles[1]
del motorcycles[-1]
motorcycles[0] = 'honda'
print(motorcycles)

popped_element = motorcycles.pop()
print(popped_element)
print(motorcycles)
motorcycles.insert(-1, 'suzuki')
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)
trash_bike = 'suzuki'
motorcycles.remove(trash_bike)
print(motorcycles)

# organizing a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars, reverse=False))
cars.sort()
print(cars)
cars.reverse()
print(cars)
print(len(cars))
cars[len(cars)-1] = 'Acura'
print(cars)
