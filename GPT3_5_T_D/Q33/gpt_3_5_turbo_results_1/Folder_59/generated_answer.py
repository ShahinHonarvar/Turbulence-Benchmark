
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for char in string[8:9]:
        if char.lower() in vowels and 'Y' < char.lower() <= 's':
            result.append(char)
    
    return result
