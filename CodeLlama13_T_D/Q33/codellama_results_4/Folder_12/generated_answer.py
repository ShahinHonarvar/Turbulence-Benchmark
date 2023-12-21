
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[13:37] if char > 'Z' and char <= '}' and char in vowels]
