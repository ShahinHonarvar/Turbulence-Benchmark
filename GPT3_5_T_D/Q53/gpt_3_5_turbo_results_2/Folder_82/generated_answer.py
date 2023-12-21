
import re
def palindrome_of_length_at_least_n(string):
    palindromes = set()
    sanitized_string = re.sub("[^a-zA-Z]", "", string.lower())
    n = len(sanitized_string)
    for i in range(n):
        for j in range(i + 72, n + 1):
            substring = sanitized_string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
