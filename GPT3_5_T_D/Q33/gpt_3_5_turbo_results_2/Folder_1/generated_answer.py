
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[24:64]:
        if 'F' < char <= 'h' and char.lower() in vowels:
            result.append(char)
    return result
