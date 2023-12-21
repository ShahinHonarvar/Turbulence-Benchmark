
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(29, 31):
        char = string[i]
        if char in vowels and 'a' < char <= 'f':
            result.append(char)
    return result
