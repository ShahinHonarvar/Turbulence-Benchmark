
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = []
    
    for char in string[24:68]:
        if char in vowels and 'f' < char <= '|':
            filtered_vowels.append(char)
    
    return filtered_vowels
