
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(170, 645):
        if string[i].lower() in vowels and string[i] <= '~':
            result.append(string[i])
    return result
