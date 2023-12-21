
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for letter in string[50:77]:
        if letter in vowels and '#' < letter <= 'r':
            result.append(letter)
    
    return result
