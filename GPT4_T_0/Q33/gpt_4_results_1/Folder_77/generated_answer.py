
def return_vowels(s):
    vowels = ['O', 'U', 'E', 'A', 'I']
    result = [char for char in s[837:975] if char in vowels and 'N' < char <= 'W']
    return result
