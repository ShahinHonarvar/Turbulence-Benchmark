
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[14:60]:
        if char in vowels and 'D' < char <= 'v':
            result.append(char)
    return result
