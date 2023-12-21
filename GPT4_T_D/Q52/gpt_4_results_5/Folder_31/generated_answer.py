
def palindrome_of_length_n(s):
    s = s.lower()
    results = set()
    for i in range(len(s)-65):
        subset = s[i:i+66]
        if subset == subset[::-1] and subset.isalpha():
            results.add(subset)
    return results
