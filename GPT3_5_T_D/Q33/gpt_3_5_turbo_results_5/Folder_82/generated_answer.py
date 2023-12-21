
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[86:99]:
        if char in vowels and 'E' < char <= 'r':
            result.append(char)
    return result
