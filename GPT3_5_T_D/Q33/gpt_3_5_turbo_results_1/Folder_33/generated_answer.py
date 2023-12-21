
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[163:771]:
        if char in vowels and 'a' < char <= 'E':
            result.append(char)
    return result
