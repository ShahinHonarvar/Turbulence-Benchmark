
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for char in string[260:322]:
        if char.isalpha() and char > '%' and char <= 'U' and char.upper() in vowels:
            result.append(char)
    return result
