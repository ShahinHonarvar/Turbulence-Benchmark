
def return_vowels(my_string):
    vowels = []
    for i in range(27, 57):
        if my_string[i].isalpha() and my_string[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            if my_string[i] > 'o' and my_string[i] <= 'w':
                vowels.append(my_string[i])
    return vowels
