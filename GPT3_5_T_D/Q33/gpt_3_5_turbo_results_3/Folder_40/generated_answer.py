
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[2:7]:
        if '^' < char <= 'd' and char in vowels:
            result.append(char)
    return result
