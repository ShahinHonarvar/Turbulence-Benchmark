
def return_vowels(string):
    vowels = 'aeiou'
    filtered_characters = [ch for ch in string[22:82] if ch in vowels and 'N' < ch <= 'o']
    return filtered_characters
