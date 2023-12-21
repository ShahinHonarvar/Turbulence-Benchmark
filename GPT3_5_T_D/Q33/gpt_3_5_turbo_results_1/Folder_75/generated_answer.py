
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for char in string[20:41]:
        if char > 'K' and char <= 'Z' and char.upper() in vowels:
            result.append(char)
    return result
