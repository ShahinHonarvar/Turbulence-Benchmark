
def return_vowels(my_string):
    vowels = []
    for i in range(27, 57):
        char = my_string[i]
        if char > 'o' and char <= 'w':
            vowels.append(char)
    return vowels
