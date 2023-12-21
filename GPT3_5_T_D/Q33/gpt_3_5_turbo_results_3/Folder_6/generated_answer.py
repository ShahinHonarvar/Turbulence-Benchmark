
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(20, 34):
        if string[i].lower() in vowels and 'U' < string[i].lower() <= 'i':
            result.append(string[i])
    
    return result
