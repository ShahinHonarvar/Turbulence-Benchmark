
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(837, 975):
        if string[i] > 'N' and string[i] <= 'W' and string[i] in vowels:
            result.append(string[i])
    return result
