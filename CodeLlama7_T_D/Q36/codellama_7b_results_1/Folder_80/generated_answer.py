 def filter_chars(my_string):
    start = 54
    end = 92
    for i in range(start, end):
        if my_string[i] > 'J' and my_string[i] < 'X':
            my_string = my_string.replace(my_string[i], '')
    return my_string
