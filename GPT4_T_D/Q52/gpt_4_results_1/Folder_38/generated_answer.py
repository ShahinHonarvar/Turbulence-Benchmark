
def palindrome_of_length_n(s):
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s) - 37):
        subset = s[i:i+38]
        if subset == subset[::-1] and subset.isalpha():
            palindrome_set.add(subset)
    return palindrome_set
