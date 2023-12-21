
def palindrome_of_length_n(s):
    s = s.lower()
    results = set()
    for i in range(len(s)):
        for j in range(i + 73, min(i + 146, len(s) + 1)): 
            segment = s[i:j]
            if segment == segment[::-1] and segment.isalpha():
                results.add(segment)

    return results
