
def return_vowels(my_string):
    vowels = []
    for i in range(56, 91):
        if my_string[i].isalpha() and my_string[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            if my_string[i] > 'K' and my_string[i] <= 'z':
                vowels.append(my_string[i])
    return vowels
