
def return_vowels(my_string):
    vowels = []
    for i in range(20, 43):
        if my_string[i].isalpha() and my_string[i].islower():
            if my_string[i] > '5' and my_string[i] <= 'M':
                vowels.append(my_string[i])
    return vowels
