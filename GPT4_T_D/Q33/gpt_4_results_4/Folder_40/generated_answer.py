
def return_vowels(s):
    vowel_chars = 'aeiou'
    filtered_chars = [char for char in s[2:7] if char > '^' and char <= 'd' and char in vowel_chars]
    return filtered_chars
