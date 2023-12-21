
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for char in string[1:5]:
        if '!' < char <= 'j' and char in vowels:
            result.append(char)
    
    return result
