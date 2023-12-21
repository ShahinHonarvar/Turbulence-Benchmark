
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(74, 96):
        if string[i].lower() in vowels and 'I' < string[i].lower() <= 'X':
            result.append(string[i])
    return result
