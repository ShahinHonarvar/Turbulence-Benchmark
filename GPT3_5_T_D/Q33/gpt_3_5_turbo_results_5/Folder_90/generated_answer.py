
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(142, 145):
        if string[i].lower() in vowels and string[i].lower() > 'd' and string[i].lower() <= 'o':
            result.append(string[i])
    
    return result
