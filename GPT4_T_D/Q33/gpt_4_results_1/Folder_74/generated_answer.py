
def return_vowels(s):
    vowels = set('aeiouAEIOU')
    special_chars = [c for c in s[69:82] if '[' < c <= '~']
    return [c for c in special_chars if c in vowels]
