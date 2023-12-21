
def remove_repeat_chars(s):
    in_range_repeats = [char for char, count in 
                        dict.fromkeys(s[30:53]).items() if s[30:53].count(char) > 1]
    return ''.join(char for char in s if char not in in_range_repeats)
