
def return_vowels(my_string):
    vowels = []
    for i in range(24, 68 + 1):
        if my_string[i].lower() in ['a', 'e', 'i', 'o', 'u'] and my_string[i] > 'f' and my_string[i] <= '|':
            vowels.append(my_string[i])
    return vowels
