
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[24:64]:
        if char in vowels and 'F' < char <= 'h':
            result.append(char)
    return result
