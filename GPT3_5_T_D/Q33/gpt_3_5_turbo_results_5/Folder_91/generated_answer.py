
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o','u']
    result = []
    for char in string[4:8]:
        if char in vowels and ord('P') < ord(char) <= ord('r'):
            result.append(char)
    return result
