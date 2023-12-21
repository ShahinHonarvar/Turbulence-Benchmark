
def return_vowels(s):
    vowels = 'aeiou'
    sub_str = s[604:949].lower()
    selected_chars = [char for char in sub_str if char in vowels and 'n' < char <= 'u']
    return selected_chars
