
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[17:65]:
        if char in vowels and char > 'U' and char <= '{':
            result.append(char)
    return result
