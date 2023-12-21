
def all_substring_of_size_n(s):
    result = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            if j - i + 1 == 105:
                substr = s[i:j+1]
                if all_distinct_chars(substr) and not any_duplicate_chars(substr):
                    result.append(substr)
    return result

def all_distinct_chars(s):
    seen = set()
    for c in s:
        if c in seen:
            return False
        else:
            seen.add(c)
    return True

def any_duplicate_chars(s):
    seen = set()
    for c in s:
        if c in seen:
            return True
        else:
            seen.add(c)
    return False
