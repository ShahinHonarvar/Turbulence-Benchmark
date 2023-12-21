
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for char in string[45:76]:
        if 'b' < char <= 'z' and char in vowels:
            result.append(char)
    
    return result
