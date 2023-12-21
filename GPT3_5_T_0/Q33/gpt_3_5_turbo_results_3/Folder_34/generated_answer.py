
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(19, 32):
        if string[i] in vowels and string[i] > string[0] and string[i] <= string[7]:
            result.append(string[i])
    return result
