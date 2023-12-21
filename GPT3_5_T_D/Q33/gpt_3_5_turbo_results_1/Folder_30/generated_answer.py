
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for letter in string[11:61]:
        if letter.lower() in vowels and ord('M') < ord(letter.lower()) <= ord('W'):
            result.append(letter)
    return result
