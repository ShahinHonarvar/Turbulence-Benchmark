
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[4:8]:
        if 'P' < char <= 'r' and char in vowels:
            result.append(char)
    return result
