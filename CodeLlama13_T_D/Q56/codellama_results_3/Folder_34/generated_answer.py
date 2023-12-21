
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substring = string[i:j]
            if len(substring) == 84 and all_unique_chars(substring):
                substrings.append(substring)
    return substrings

def all_unique_chars(string):
    seen = set()
    for char in string:
        if char in seen:
            return False
        seen.add(char)
    return True
