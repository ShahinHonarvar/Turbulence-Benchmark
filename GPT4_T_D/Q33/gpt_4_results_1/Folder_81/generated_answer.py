
def return_vowels(string):

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    result = []

    for char in string[20:43]:
        if char in vowels and '5' < char <= 'M':
            result.append(char)

    return result
