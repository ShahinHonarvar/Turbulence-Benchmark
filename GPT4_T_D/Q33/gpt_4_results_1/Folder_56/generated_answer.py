
def return_vowels(string):
    vowels = "aeiouAEIOU"
    return [char for char in string[15:86] if char in vowels and '@' < char <= '~']
