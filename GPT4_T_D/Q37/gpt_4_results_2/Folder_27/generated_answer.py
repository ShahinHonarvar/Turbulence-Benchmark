
def filter_chars(s):
    end = min(80, len(s))
    special_chars = set([char for char in s[43:end+1] if '=' <= char <= 'E'])
    result = ''.join([char for char in s if char not in special_chars])
    return result
