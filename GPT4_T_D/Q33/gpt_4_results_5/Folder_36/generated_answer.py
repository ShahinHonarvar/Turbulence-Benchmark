
def return_vowels(s):
    vowels = ['O', 'U', 'E', 'I', 'A']
    low_pos = 604
    high_pos = 949
    letter_range = s[low_pos:high_pos]
    valid_letters = [let for let in letter_range if let in vowels]
    return valid_letters
