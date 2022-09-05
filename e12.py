import functions12
first_number = int(input("Write first number: "))
second_number = int(input("Write second number: "))
print(functions12.sum(first_number, second_number))

print(functions12.cube(first_number))

distance = int(input("The distance you walked in meters: "))
step_length = float(input("The length of your step in meters: "))
print(functions12.steps_counter(distance, step_length))

first_numb = int(input("Write first number: "))
second_numb = int(input("Write second number: "))
print(functions12.absolute_diff(first_numb, second_numb))