
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    for character in string[32:97]:
        if 'Q' < character <= ']':
            if character in vowels:
                result.append(character)
    return result
