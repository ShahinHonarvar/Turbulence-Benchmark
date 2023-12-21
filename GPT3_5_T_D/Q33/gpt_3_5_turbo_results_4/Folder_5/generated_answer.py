
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(44, 95):
        if 5 < ord(string[i]) <= ord('<') and string[i] in vowels:
            result.append(string[i])
    return result
