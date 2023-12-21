
def return_vowels(string):
    vowels = "aeiouAEIOU"
    result = []
    for char in string[40:94]:
        if char in vowels and ord(char) > ord('4') and ord(char) <= ord('H'):
            result.append(char)
    return result
