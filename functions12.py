def sum(a, b):
    c = a + b
    return f"Sum is {c}"

def cube(a):
    cube = a*a*a
    return f"Cube is {cube}"

def steps_counter(distance, step_length):
    step_number = distance / step_length
    return f"The number of steps you made: {step_number}"

def absolute_diff(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1
