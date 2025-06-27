student_list = ["john", "jane", "joe", "jack", "zoe", "juli", "zach", "alex", "jules", "gary"]
grades_list = [67, 43, 78, 92, 97, 54, 59, 73, 84, 85]
grades_dictionary = {student_list[0]:grades_list[0], student_list[1]:grades_list[1], student_list[2]:grades_list[2], student_list[3]:grades_list[3], student_list[4]:grades_list[4], student_list[5]:grades_list[5], student_list[6]:grades_list[6], student_list[7]:grades_list[7], student_list[8]:grades_list[8], student_list[9]:grades_list[9]}
# {} curly brackets are used for dictionaries

print(grades_dictionary)

for k, v in grades_dictionary.items():
    print(k, ":", v)

fruit_prices = {"lychee":10, "apple":5, "mango":12, "pear":8, "orange":4, "dragon fruit":15}
print(fruit_prices.keys()) # k stands for keys and prints out the keys of a dictionary
print(fruit_prices.values()) # v stands for values and prints out the values of a dictionary
print(fruit_prices.items()) # prints out the key value pairs of a dictionary

for k, v in fruit_prices.items():
    print(k, ":", v)

