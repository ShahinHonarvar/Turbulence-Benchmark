
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[3:9]:
        if char in vowels and 'S' < char <= 'U':
            result.append(char)
    return result
