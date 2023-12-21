
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    selected_vowels = []
    
    for i in range(47, 61):
        if string[i] > '9' and string[i] <= 'O' and string[i].lower() in vowels:
            selected_vowels.append(string[i])
    
    return selected_vowels
