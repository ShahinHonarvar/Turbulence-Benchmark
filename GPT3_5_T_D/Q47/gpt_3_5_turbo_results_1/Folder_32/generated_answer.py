
def palindromes_of_specific_lengths(string):
    palindrome_set = set()
    substring = string[16:78].lower()
    for length in range(43, 48):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindrome_set.add(sub)
    return palindrome_set
