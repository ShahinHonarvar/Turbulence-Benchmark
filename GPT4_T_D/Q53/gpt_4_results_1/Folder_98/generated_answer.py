
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i+6, len(s)+1):
            slice_s = s[i:j]
            if slice_s == slice_s[::-1] and slice_s.isalpha():
                palindrome_set.add(slice_s)
    return palindrome_set
