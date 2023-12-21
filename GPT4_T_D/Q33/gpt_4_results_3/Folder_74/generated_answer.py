
def return_vowels(s):
    vowels = 'aeiou'
    selected_chars = s[69:82]
    return [c for c in selected_chars if c.lower() in vowels and c > '[' and c <= '~']
