
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[43:70]:
        if '*' < char <= 'b' and char in vowels:
            result.append(char)
    return result
