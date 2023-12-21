
def return_vowels(string):
    vowels = 'aeiou'
    filtered_chars = [char for char in string[20:34] if (char > 'U' and char <= 'i' and char in vowels)]
    return filtered_chars
