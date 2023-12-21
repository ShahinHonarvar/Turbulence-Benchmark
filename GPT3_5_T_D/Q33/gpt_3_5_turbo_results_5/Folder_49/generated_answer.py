
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[10:97]:
        if char in vowels and char > 'R' and char <= 'b':
            result.append(char)
    return result
