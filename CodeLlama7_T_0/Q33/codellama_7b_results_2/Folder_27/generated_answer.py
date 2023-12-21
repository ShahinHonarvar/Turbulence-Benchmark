
def return_vowels(my_string):
    vowels = []
    for i in range(29, 31):
        if my_string[i].isalpha() and my_string[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            if my_string[i] > 'a' and my_string[i] <= 'f':
                vowels.append(my_string[i])
    return vowels
