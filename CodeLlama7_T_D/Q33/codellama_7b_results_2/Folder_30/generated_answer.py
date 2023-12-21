
def return_vowels(my_string):
    vowels = []
    for i in range(11, 61):
        if my_string[i].isalpha() and my_string[i].lower() in ['a', 'e', 'i', 'o', 'u'] and my_string[i] > 'M' and my_string[i] <= 'W':
            vowels.append(my_string[i])
    return vowels
