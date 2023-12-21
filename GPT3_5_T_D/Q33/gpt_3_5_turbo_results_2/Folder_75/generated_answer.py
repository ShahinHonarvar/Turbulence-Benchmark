
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[20:41]:
        if char in vowels and 'K' < char <= 'Z':
            result.append(char)
    return result
