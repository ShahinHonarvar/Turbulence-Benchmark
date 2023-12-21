
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(13, 35):
        if string[i] in vowels and ord(string[i]) > 8 and ord(string[i]) <= 0xf:
            result.append(string[i])
    return result
