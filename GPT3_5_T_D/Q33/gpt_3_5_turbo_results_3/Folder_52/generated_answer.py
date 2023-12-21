
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[24:68]:
        if 'f' < char <= '|':
            if char in vowels:
                result.append(char)
    return result
