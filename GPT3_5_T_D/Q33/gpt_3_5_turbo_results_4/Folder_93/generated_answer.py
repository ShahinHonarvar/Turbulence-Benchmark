
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(54, 82):
        if string[i] > '=' and string[i] <= '@':
            if string[i].lower() in vowels:
                result.append(string[i])
    
    return result
