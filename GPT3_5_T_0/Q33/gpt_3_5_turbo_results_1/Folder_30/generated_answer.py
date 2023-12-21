
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[11:61]:
        if char in vowels and 'M' < char <= 'W':
            result.append(char)
    return result
