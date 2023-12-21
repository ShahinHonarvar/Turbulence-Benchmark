
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[29:31]:
        if char in vowels and 'a' < char <= 'f':
            result.append(char)
    return result
