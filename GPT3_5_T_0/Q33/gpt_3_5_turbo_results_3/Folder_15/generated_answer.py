
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[5:6]:
        if char > string[3] and char <= '^' and char in vowels:
            result.append(char)
    return result
