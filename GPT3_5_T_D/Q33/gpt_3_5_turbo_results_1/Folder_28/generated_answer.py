
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[41:50]:
        if char in vowels and char > 'W' and char <= '[':
            result.append(char)
    return result
