
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[12:39]:
        if char in vowels and ';' < char <= '|':
            result.append(char)
    return result
