
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[32:97]:
        if char in vowels and 'Q' < char <= ']':
            result.append(char)
    return result
