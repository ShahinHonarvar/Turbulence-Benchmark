
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[20:34]:
        if char in vowels and 'U' < char <= 'i':
            result.append(char)
    return result
