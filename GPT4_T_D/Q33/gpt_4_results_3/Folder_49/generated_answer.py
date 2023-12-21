
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for char in string[10:97]:
        if char in vowels and 'R' < char <= 'b':
            result.append(char)
    return result
