
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[23:38]:
        if char in vowels and 'N' < char <= 'k':
            result.append(char)
    return result
