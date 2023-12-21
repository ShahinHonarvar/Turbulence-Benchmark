
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[24:64]:
        if char.lower() in vowels and 'G' < char.lower() <= 'h':
            result.append(char)
    return result
