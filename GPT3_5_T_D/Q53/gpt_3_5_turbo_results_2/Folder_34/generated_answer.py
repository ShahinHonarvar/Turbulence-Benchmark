
def palindrome_of_length_at_least_n(string):
    palindromes = set()
    lower_string = string.lower()
    for i in range(len(lower_string)-67):
        for j in range(68, len(lower_string)-i+1):
            substr = lower_string[i:i+j]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes
