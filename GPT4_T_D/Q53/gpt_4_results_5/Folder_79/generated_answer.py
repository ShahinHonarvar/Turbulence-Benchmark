
def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 17, len(string) + 1):
            temp_str = string[i: j]
            if temp_str.lower() == temp_str[::-1].lower() and temp_str.isalpha():
                palindromes.add(temp_str.upper())
    return palindromes
