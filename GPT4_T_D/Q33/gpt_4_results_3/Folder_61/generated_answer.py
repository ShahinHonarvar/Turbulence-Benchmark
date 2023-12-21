
def return_vowels(string):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    chars = [char for char in string[1:4] if 'C'<char<='I' and char in vowels]
    return chars
