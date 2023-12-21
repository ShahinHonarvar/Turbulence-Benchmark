
def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    eligible_chars = [char for char in s[74:96] if 'I' < char <= 'X' and char in vowels]
    return eligible_chars
