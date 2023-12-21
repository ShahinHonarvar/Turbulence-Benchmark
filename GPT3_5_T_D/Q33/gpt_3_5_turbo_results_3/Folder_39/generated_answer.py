
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[32:97]:
        if 'Q' < char <= ']':
            if char.lower() in vowels:
                result.append(char)
    return result
