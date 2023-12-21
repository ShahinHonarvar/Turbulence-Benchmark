
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[46:90]:
        if char in vowels and char > '@' and char <= '[':
            result.append(char)
    return result
