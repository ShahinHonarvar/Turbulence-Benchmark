
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for char in string[64:82]:
        if 'P' < char <= 'z' and char.lower() in vowels:
            result.append(char)
    
    return result
