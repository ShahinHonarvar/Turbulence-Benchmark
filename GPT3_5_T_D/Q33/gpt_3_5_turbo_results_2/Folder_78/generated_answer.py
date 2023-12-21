
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(46, 90):
        if string[i] in vowels and string[i] > '@' and string[i] <= '[':
            result.append(string[i])
    
    return result
