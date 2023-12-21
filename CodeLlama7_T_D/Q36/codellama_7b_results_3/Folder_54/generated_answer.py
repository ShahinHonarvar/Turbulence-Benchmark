 def filter_chars(my_string):
    # Get the indices of the characters between 18 and 38 (exclusive)
    start = my_string.index('(', 18)
    end = my_string.index('P', 18)
    # Create a new string with the filtered characters
    filtered_string = ''
    for i in range(start, end):
        if my_string[i] > ')' and my_string[i] < 'P':
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
