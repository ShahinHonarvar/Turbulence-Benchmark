
def all_substring_of_size_n(s):
    n = 120
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if len(substring) == n and all_unique_chars(substring):
                substrings.append(substring)
    return substrings

def all_unique_chars(s):
    seen = set()
    for c in s:
        if c in seen:
            return False
        seen.add(c)
    return True
