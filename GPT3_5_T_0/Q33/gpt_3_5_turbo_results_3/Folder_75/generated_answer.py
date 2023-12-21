
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[20:41]:
        if char in vowels and 'K' < char <= 'Z':
            result.append(char)
    return result
