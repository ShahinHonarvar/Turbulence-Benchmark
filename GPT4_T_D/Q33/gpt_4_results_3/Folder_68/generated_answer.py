
def return_vowels(string):
    vowels = "aeiou"
    return [char for char in string[1:9] if char in vowels and 'a' <= char <= 'k']
