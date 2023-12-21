
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[24:59]:
        if char in vowels and 'N' < char <= 'U':
            result.append(char)
    return result
