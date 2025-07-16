def square():
    side = int(input("Enter side of square: "))
    area_square = side * side
    print("Area of square: ", area_square)
    

def rectangle():
    length = int(input("Enter length of rectangle: "))
    width = int(input("Enter width of rectangle: "))
    area_rectangle = length * width
    print("Area of rectangle: ", area_rectangle)

def triangle():
    height = int(input("Enter height of rectangle: "))
    base = int(input("Enter base of triangle: "))
    area_triangle = 0.5 * height * base
    print("Area of triangle: ", area_rectangle)

ch = 1
while ch:
    print("Press 1 for square")
    print("Press 2 for rectangle")
    print("Press 3 for triangle")
    choice = int(input("Make a choice: "))
    if choice == 1:
        square()
    elif choice == 2:
        rectangle()
    elif choice == 3:
        triangle()
    else:
        print("Wrong choice, try again.")
    ch = int(input("Press 0 to stop, else continue"))
