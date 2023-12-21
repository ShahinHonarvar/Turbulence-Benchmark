
def return_vowels(string):
    vowels = 'aeiouAEIOU'
    selected_vowels = []
    for i in range(23, 38):
        if string[i].isalpha() and string[i].upper() in vowels and 'N' < string[i].upper() <= 'K':
            selected_vowels.append(string[i])
    return selected_vowels
