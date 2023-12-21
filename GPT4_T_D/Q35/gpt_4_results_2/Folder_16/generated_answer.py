
def remove_repeat_chars(s):
    subset = s[91:97]
    repeats = [ch for ch in subset if subset.count(ch) > 1]
    result = ''.join([ch for ch in s if ch not in repeats])
    return result
