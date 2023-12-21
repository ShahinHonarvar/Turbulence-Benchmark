
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[55:65]:
        if char in vowels and 'Z' < char <= 'w':
            result.append(char)
    return result
