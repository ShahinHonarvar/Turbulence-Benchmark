
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(56, 90):
        if string[i] > 'K' and string[i] <= 'z' and string[i].lower() in vowels:
            result.append(string[i])
    
    return result
