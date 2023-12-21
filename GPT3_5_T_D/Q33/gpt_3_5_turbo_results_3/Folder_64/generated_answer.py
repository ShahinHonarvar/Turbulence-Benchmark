
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for c in string[1:7]:
        if 'F' < c <= 'j' and c.lower() in vowels:
            result.append(c)
    
    return result
