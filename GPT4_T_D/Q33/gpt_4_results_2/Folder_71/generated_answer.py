
def return_vowels(string):
    vowels = "aeiou"
    valid_chars = [chr(i) for i in range(ord('+')+1, ord('/')+1) if chr(i) in vowels]
    return [char for char in string[36:56] if char in valid_chars]
