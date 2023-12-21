
def palindrome_of_length_n(s):
    s_lower = s.lower()
    results = set()

    for i in range(len(s_lower) - 56):
        substring = s_lower[i:i+57]
        if substring == substring[::-1] and all(c.isalpha() for c in substring):
            results.add(substring)

    return results
