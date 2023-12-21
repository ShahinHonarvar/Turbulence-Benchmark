
def return_vowels(input_str):
    vowels = ['A', 'E', 'I', 'O','U','a','e','i','o','u']
    chars = list(input_str[56:68])
    chars = filter(lambda x: 'M' < x <= 'X' and x in vowels, chars)
    return list(chars)
