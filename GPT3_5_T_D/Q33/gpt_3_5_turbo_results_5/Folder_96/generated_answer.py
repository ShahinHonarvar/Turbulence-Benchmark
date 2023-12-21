
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[77:84]:
        if char in vowels and char > '(' and char <= 'G':
            result.append(char)
    return result
