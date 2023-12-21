
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(56, 90):
        if string[i].lower() in vowels and string[i] > 'k' and string[i] <= 'z':
            result.append(string[i])
    return result
