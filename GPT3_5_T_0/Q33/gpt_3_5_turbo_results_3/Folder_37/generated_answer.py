
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[82:90]:
        if char in vowels and 'T' < char <= 'b':
            result.append(char)
    return result
