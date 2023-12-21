
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for c in string[37:57]:
        if '*' < c <= 'P' and c.lower() in vowels:
            result.append(c)
    
    return result
