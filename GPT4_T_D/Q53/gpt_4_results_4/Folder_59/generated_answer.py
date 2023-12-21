
def palindrome_of_length_at_least_n(s):
    palindrome_set = set()
    s = ''.join(filter(str.isalpha, s.lower()))
    
    for i in range(len(s)):
        for j in range(i+20, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                palindrome_set.add(s[i:j])

    return palindrome_set
