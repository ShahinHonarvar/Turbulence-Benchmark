
def palindromes_of_specific_lengths(string):
    sub_str = string[0:30]  # substring from index 0 to index 30, both inclusive
    palindromes = set()
    for i in range(20, 31):  # lengths between 20 to 30 (both inclusive)
        for j in range(len(sub_str) - i + 1):
            substr = sub_str[j:j+i]
            if substr == substr[::-1]:  # check if substring is palindrome
                palindromes.add(substr)
    return palindromes
