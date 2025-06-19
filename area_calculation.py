'''
Find:
1. Find the area of the square
2. Find the area of the triangle
3. Find the area of the rectangle
condition = "S" 
condition = "T"
condition = "R"
'''

condition = input("Enter the condition: ")
if condition == "S":
    side = int(input("Enter one side of the square: "))
    area_of_square = side * side
    print("The area of the square is:", area_of_square)
elif condition == "T":
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    area_of_triangle = base * height / 2
    print("The area of the triangle is:", area_of_triangle)
elif condition == "R":
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))
    area_of_rectangle = width * height
    print("The area of the rectangle is:", area_of_rectangle)
else :
    print("Wrong condition, please enter S, T, or R.")