
def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s)):
        if s[i].isalpha():
            for j in range(i+1, len(s)):
                if s[j-i-1] == s[j]:
                    if len(palindromes) > 0:
                        break
                    else:
                        palindromes.add(s[i:j])
    return palindromes
