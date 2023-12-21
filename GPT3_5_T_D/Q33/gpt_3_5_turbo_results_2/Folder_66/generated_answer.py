
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[63:79]:
        if char in vowels and char > 'D' and char <= 'y':
            result.append(char)
    return result
