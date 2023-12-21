
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(24, 64):
        if string[i].lower() in vowels and string[i] > 'f' and string[i] <= 'h':
            result.append(string[i])
    return result
