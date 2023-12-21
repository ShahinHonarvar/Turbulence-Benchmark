
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[71:88]:
        if char.isalpha() and char.lower() in vowels and ord(char) > ord('9') and ord(char) <= ord('P'):
            result.append(char)
    return result
