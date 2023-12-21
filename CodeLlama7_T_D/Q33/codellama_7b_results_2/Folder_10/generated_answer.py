
def return_vowels(my_string):
    vowels = []
    for i in range(31, 37):
        if my_string[i] > ';' and my_string[i] <= 't':
            vowels.append(my_string[i])
    return vowels
