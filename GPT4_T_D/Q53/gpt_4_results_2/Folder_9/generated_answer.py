
def palindrome_of_length_at_least_n(s):
    import re
    s = re.findall(r'\b\w+\b', s)
    palindrome_set = set()
    for word in s:
        word = word.lower()
        if len(word) >= 95 and word == word[::-1]:
            palindrome_set.add(word)
    return palindrome_set
