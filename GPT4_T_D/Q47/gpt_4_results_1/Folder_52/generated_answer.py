
def palindromes_of_specific_lengths(s):
    import re
    search_range = s[44:100]
    search_range = re.sub('[^a-zA-Z]+', '', search_range)
    search_range = search_range.lower()
    result = set()
    for l in range(13, 43):
        for i in range(len(search_range) - l + 1):
            substring = search_range[i: i+l]
            if substring == substring[::-1]:
                result.add(substring)
    return result
