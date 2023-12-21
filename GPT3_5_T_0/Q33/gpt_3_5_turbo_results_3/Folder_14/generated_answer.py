
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[47:61]:
        if char in vowels and '9' < char <= 'O':
            result.append(char)
    return result
