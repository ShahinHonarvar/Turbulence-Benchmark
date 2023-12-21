 def filter_chars(my_string):
    for i in range(77, 87):
        if my_string[i] > ';' and my_string[i] < 'r':
            my_string = my_string[:i] + my_string[i+1:]
    return my_string
