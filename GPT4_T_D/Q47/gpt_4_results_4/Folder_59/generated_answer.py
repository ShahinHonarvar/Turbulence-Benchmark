
def palindromes_of_specific_lengths(string):
    subset = string.lower()[0:101]
    palindrome_set = set()
    for i in range(len(subset)):
        for j in range(i + 3, i + 16):
            substring = subset[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring)
    return palindrome_set
