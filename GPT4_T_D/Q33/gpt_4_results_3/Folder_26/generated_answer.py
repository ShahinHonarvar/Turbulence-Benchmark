
def return_vowels(string):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    return [char for char in string[10:82] if char > '$' and char <= '@' and char in vowels]
