
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = []
    for char in string[23:38]:
        if char in vowels and 'N'< char <= 'k':
            output.append(char)
    return output
