
def palindrome_of_length_n(s):
    s = s.lower()
    results = set()
    for i in range(len(s)):
        for j in range(i+27, len(s)+1):
            subset = s[i:j]
            if subset == subset[::-1] and subset.isalpha():
                results.add(subset)
    return results
