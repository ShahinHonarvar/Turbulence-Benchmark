
def return_vowels(string):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    substring = string[71:81]
    valid_chars = [char for char in substring if char in vowels 
                   and char > '>' and char <= 'U']
    return valid_chars
