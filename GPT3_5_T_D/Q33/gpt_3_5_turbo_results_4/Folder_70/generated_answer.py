
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[171:402]:
        if char in vowels and 'I' < char <= 'k':
            result.append(char)
    return result
