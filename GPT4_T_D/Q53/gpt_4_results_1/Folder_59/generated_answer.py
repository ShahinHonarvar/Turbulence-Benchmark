
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()

    for i in range(len(s)):
        for j in range(i + 20, len(s) + 1):
            temp = s[i:j]
            if temp == temp[::-1] and temp.isalpha():
                palindromes.add(temp)

    return palindromes
