
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s_new = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for i in range(len(s_new)-10):
        for j in range(i+11, len(s_new)+1):
            if s_new[i:j] == s_new[i:j][::-1]:
                palindromes.add(s_new[i:j])
    return palindromes
