
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(32, 61):
        if string[i] > '?' and string[i] <= 'P' and string[i].lower() in vowels:
            result.append(string[i].lower())
    return result
