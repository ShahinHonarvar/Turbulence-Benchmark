
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []

    for char in string[528:606]:
        if char in vowels and 'M' < char <= 'X':
            result.append(char)
    
    return result
