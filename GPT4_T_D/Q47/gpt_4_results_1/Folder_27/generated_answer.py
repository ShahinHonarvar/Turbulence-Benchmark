
def palindromes_of_specific_lengths(s):
    palindrome_set = set()
    s = s[13:100]
    s = ''.join([i for i in s if i.isalpha()])
    for i in range(len(s)):
        for j in range(i+26, min(i+30, len(s)+1)):
            sub_str = s[i:j]
            if sub_str.lower() == sub_str.lower()[::-1]:
                palindrome_set.add(sub_str)
    return palindrome_set
