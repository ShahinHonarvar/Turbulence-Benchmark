
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[47:61]:
        if char in vowels and ord(char) > ord('9') and ord(char) <= ord('O'):
            result.append(char)
    return result
