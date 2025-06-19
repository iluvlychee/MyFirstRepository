signal = input("Enter the color of the traffic signal: ")

if signal == (signal == "Green") or signal == "green":
    print("Start driving!")
elif (signal == "Yellow") or (signal == "yellow"):
    print("Start the engine of your car!")
else:
    print("Don't start the car!")

# this code is case senstive, which is why we use the "or" operator to check for both "Yellow" and "yellow".
# if none of the input matches the conditions, it will print "Don't start the car!" because of the "else"
# since the input is not "Green" or "green" or "Yellow" or "yellow", it will print "Don't start the car!".
# if the input is "Green" or "green", it will print "Start driving!".
# if the input is "Yellow" or "yellow", it will print "Start the engine of your car!".
# if printed "Red", the program will not understand it and will print "Don't start the car!".