
def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    letter_range = s[74:96]
    vowels_in_range = [letter for letter in letter_range if letter in vowels and 'I' < letter <= 'X']
    return vowels_in_range
