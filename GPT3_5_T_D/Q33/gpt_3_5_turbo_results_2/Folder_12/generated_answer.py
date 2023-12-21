
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for char in string[13:37]:
        if 'Z' < char <= '}':
            if char in vowels:
                result.append(char)
    
    return result
