
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[34:58]:
        if char in vowels and 'b' < char <= 'o':
            result.append(char)
    return result
