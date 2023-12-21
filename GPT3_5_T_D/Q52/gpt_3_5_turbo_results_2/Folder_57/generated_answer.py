
def palindrome_of_length_n(string):
    palindromes = set()
    length = 92

    for i in range(len(string)-length+1):
        substring = string[i:i+length]
        substring_lower = substring.lower()
        if substring_lower == substring_lower[::-1] and substring.isalpha():
            palindromes.add(substring)

    return palindromes
