
def return_vowels(text):
    vowels = ['O', 'I', 'E', 'A', 'U']
    substring = text[22:82]
    vowels_in_substr = [char for char in substring if char in vowels]
    return [char for char in vowels_in_substr if 'N' < char <= 'o']
