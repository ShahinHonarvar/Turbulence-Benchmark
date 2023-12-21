 
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    selected_vowels = []
    for i in range(11, 61):
        if string[i].lower() in vowels and string[i] > 'M' and string[i] <= 'W':
            selected_vowels.append(string[i])
    return selected_vowels
