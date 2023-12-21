
def return_vowels(string):
    vowels = set('aeiou')
    letters_in_range = [ch for ch in string[529:828] if 'U'<ch<='l' and ch.lower() in vowels]
    return letters_in_range
