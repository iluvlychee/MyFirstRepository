car_brands = ["ferrari", "aston martin", "mclaren", "audi", "mercedes"]
for names in car_brands:
    print(names)

bike_brands = ["yamaha", "honda", "ktm", "bmw", "hyabuza"]
print(bike_brands[4])
print(len(bike_brands))

fruits = ["apple", "pear", "orange", "strawberry", "banana", "blueberry", "raspberry", "mango", "lychee", "dragon fruit"]
print("there are", len(fruits), "fruits in this list") # len(variable) helps determine the lenght of a list
print(fruits[1:5]) # this technique is called list slicing. lists start from 0.
print(fruits[2:len(fruits)]) 

vegetable1 = ["carrot", "broccoli", "greenbean"]
vegetable2 = ["cauliflower", "edemame", "brussel sprout", "spinach", "celery"]
vegetable = vegetable1 + vegetable2
print(vegetable)

numbers = [44, 88, 22, 55, 77]
added = vegetable1 + numbers
print(added)

mixed_list = [2, 5, "john", "jane", 11.5, 66.3]
print(mixed_list)