
def all_substring_of_size_n(string, n):
    substrings = []
    for i in range(len(string)):
        for j in range(i+1, len(string)-n+1):
            substring = string[i:j]
            if len(set(substring)) == n and all_distinct_chars(substring):
                substrings.append(substring)
    return substrings

def all_distinct_chars(string):
    seen = set()
    for char in string:
        if char in seen:
            return False
        seen.add(char)
    return True
