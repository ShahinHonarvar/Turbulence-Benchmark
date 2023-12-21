
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(163, 771):
        if string[i] in vowels and string[i] > ':' and string[i] <= 'E':
            result.append(string[i])
    return result
