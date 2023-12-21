
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(85, 99):
        char = string[i]
        if char in vowels and '/' < char <= 'n':
            result.append(char)
    return result
