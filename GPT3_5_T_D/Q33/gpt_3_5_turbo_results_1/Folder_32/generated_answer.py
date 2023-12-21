
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[45:76]:
        if char in vowels and 'b' < char <= 'z':
            result.append(char)
    return result
