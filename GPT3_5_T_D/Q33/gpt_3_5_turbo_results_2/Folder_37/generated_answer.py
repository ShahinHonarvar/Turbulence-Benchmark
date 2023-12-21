
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[82:90]:
        if 'T' < char <= 'b' and char.lower() in vowels:
            result.append(char)
    return result
