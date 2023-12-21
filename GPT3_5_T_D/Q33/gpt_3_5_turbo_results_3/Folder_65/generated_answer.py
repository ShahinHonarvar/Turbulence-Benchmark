
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    selected_vowels = []
    
    for index in range(71, 88):
        if string[index] in vowels and string[index] > '9' and string[index] <= 'P':
            selected_vowels.append(string[index])
    
    return selected_vowels
