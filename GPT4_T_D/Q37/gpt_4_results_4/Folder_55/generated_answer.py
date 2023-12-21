
def filter_chars(s):
    chars = set(s[1:6])
    filtered_chars = [ch for ch in chars if '$' <= ch <= ';']
    result = ""
    for ch in s:
        if ch not in filtered_chars:
            result += ch
    return result
