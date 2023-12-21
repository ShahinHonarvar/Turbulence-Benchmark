
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for index in range(63, 79):
        character = string[index]
        if character in vowels and 'D' < character <= 'y':
            result.append(character)
    
    return result
