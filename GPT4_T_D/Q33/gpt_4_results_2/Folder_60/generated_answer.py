
def return_vowels(string):
    vowels = 'aeiou'
    filtered_vowels = [ch for ch in string[24:59] if ch.lower() in vowels and 'n' < ch.lower() <= 'u']
    return filtered_vowels
