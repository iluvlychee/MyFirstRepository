student_list = ["john", "jane", "joe", "jack", "zoe", "juli", "zach", "alex", "jules", "gary"]
grades_list = [67, 43, 78, 92, 97, 54, 59, 73, 84, 85]
print(len(grades_list))

for i in range(len(student_list)):
    # print(i) # i is a variable that is used as an address
    print(student_list[i], ":", grades_list[i])