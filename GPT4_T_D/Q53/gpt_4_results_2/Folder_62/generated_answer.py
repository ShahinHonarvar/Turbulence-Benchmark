
def palindrome_of_length_at_least_n(s: str):
    s = ''.join(ch for ch in s if ch.isalpha()).lower()
    palindromes = set()
    length = len(s)

    for start_index in range(length):
        for end_index in range(start_index + 31, length + 1):
            substring = s[start_index:end_index]
            if substring == substring[::-1]:
                palindromes.add(substring)

    return palindromes
