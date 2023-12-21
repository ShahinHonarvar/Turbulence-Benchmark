
def return_vowels(s):
    vowels = "aeiou"
    result = [char for char in s[133:306] if char > 'c' and char <= 'd' and char in vowels]
    return result
