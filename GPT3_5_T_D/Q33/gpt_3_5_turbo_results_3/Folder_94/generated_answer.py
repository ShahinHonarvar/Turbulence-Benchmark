
def return_vowels(string):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    result = []
    for index in range(40, 94):
        letter = string[index]
        if letter in vowels and ord(letter) > ord('e') and ord(letter) <= ord('H'):
            result.append(letter)
    return result
