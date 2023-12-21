
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(529, 828):
        if string[i].lower() in vowels and 'U' < string[i].lower() <= 'l':
            result.append(string[i])
    
    return result
