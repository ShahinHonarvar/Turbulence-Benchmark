
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[34:69]:
        if char in vowels and char > '_' and char <= 'o':
            result.append(char)
    return result
