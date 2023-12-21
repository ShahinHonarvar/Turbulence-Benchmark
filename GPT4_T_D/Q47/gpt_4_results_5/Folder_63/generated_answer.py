
def palindromes_of_specific_lengths(input_string):
    input_substring = input_string[33:86]
    palindrome_set = set()
    for length in range(26, 32):
        for i in range(len(input_substring) - length + 1):
            sub = input_substring[i: i + length]
            if sub.lower() == sub[::-1].lower() and sub.isalpha():
                palindrome_set.add(sub)
    return palindrome_set
