
def return_vowels(my_string):
    vowels = []
    for i in range(46, 91):
        if my_string[i] == '@':
            continue

        elif my_string[i] <= '[':
            vowels.append(my_string[i])
    return vowels
