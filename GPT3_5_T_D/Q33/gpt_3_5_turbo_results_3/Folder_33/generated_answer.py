
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(163, 771):
        if string[i] > ':' and string[i] <= 'E' and string[i] in vowels:
            result.append(string[i])
    return result
