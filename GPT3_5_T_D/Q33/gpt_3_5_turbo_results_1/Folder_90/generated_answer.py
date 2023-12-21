
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(142, 145):
        if 4 < ord(string[index]) <= ord('o') and string[index] in vowels:
            result.append(string[index])
    
    return result
