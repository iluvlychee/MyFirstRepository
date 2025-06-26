'''
Sports competition. The participants involved are divided into various groups based on their height.
Group E: 145cm to 155cm
Group D: 156cm to 160cm
Group C: 161cm to 175cm
Group B: 176cm to 180cm
Group A: 181cm to 190cm
'''

height_of_the_participant = int(input("Enter the height in cm: "))

if (height_of_the_participant  >= 145) and (height_of_the_participant <= 155):
    print("You belong to Group E")
elif (height_of_the_participant >= 156) and (height_of_the_participant <= 160):
    print("You belong to Group D")
elif (height_of_the_participant >= 161) and (height_of_the_participant <= 175):
    print("You belong to Group C")
elif (height_of_the_participant >= 176) and (height_of_the_participant <= 180):
    print("You belong to Group B")
elif (height_of_the_participant >= 181) and (height_of_the_participant <= 190):
    print("You belong to Group A")
else:
    print("You do not belong in any of the groups. You cannot participate.")

