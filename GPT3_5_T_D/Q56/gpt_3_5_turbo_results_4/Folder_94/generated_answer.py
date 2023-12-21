
def all_substring_of_size_n(string):
    substrings = []
    seen = set()
    length = len(string)
    
    for i in range(length - 69):
        substring = string[i:i+70]
        if len(set(substring)) == 70 and substring not in seen:
            substrings.append(substring)
            seen.add(substring)
    
    return substrings
