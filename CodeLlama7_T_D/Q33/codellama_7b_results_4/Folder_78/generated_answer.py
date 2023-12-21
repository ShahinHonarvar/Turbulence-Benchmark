
def return_vowels(my_string):
    vowels = []
    for i in range(46, 90 + 1):
        if my_string[i] in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(my_string[i])
    return vowels
