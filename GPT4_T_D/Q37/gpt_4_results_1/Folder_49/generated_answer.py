
def filter_chars(s):
    unique_chars = set(s[42:98])
    eligible_chars = {chr(i) for i in range(ord('*'), ord('b') + 1)}
    filter_chars = unique_chars.intersection(eligible_chars)
    
    result = ''.join([char for char in s if char not in filter_chars])
    return result
