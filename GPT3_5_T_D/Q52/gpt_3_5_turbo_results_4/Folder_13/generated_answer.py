
def palindrome_of_length_n(string):
    length = 206
    palindromes = set()

    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        substring_lower = substring.lower()

        if substring_lower == substring_lower[::-1] and substring_lower.isalpha():
            palindromes.add(substring)

    return palindromes
