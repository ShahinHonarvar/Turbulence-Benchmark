
def palindromes_of_specific_lengths(string):
    substring = string[101:293]
    palindrome_set = set()

    for length in range(154, 183):
        for i in range(len(substring) - length + 1):
            sub = substring[i : i + length].lower()
            if sub == sub[::-1] and sub.isalpha():
                palindrome_set.add(sub)

    return palindrome_set
