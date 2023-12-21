
def palindromes_of_specific_lengths(s):
    s = s[1:300].lower()
    relevant = "".join(ch for ch in s if ch.isalpha())
    palindrome_set = set()
    for i in range(len(relevant)):
        for j in range(i + 3, min(len(relevant) + 1, i + 11)):
            substring = relevant[i:j]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set
