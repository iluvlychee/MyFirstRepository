car_model1 = {"company name":"mercedes", "model":"amg", "year":2000}
car_model2 = {"company name":"ferrari", "model":"f340", "year":2005}
car_model3 = {"company name":"bmw", "model":"m3", "year":2007}
car_model4 = {"company name":"ford", "model":"mustang", "year":2001}
car_list = [car_model1, car_model2, car_model3, car_model4]

print(car_list)

p = list(car_model1.keys())
print(p[0], p[1], p[2])

for car in car_list:
    for _, b in car.items(): # _ is a dummy variable
        print(b, end=" ")
    print()