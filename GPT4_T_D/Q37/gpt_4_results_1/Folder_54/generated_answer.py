
def filter_chars(s: str) -> str:
    for i in range(max(len(s), 86)):
        if 46 <= i <= 85 and '-' <= s[i] <= 'X':
            s = s.replace(s[i], '')
    return s
