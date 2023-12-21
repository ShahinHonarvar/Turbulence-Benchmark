 def filter_chars(my_string):
    filtered_string = ""
    for i in range(78, 81):
        if my_string[i] > "S" and my_string[i] < "[":
            filtered_string += my_string[:i] + my_string[i+1:]
    return filtered_string
