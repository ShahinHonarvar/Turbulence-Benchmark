
def return_vowels(my_string):
    vowels = []
    for i in range(163, 771):
        if my_string[i] == ':' or my_string[i] > 'E':
            continue

        else:

            vowels.append(my_string[i])

    return vowels
