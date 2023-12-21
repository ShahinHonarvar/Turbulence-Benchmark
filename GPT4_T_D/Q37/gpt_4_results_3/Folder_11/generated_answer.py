
def filter_chars(s):
    altered_chars = [c for idx, c in enumerate(s) if not(29 <= idx <= 97 and '-' <= c <= 'n')]
    altered_string = ''.join(altered_chars)
    return altered_string
