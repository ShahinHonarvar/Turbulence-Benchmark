 def filter_chars(my_string):
    start = 43
    end = 83
    new_string = ""
    for i in range(len(my_string)):
        if my_string[i] > ":" and my_string[i] < "Q":
            continue

        else:

            new_string += my_string[i]

    return new_string
