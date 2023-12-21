
def palindromes_of_specific_lengths(string):
    # Create a set to store the palindromes
    palindromes = set()

    # Iterate over each substring of length 10-50 in the given string
    for i in range(200, 300 + 1):
        for j in range(i - 9, i + 1):
            substr = string[i:j]
            if len(substr) >= 10 and len(substr) <= 50:
                # Check if the substring is a palindrome
                if substr == substr[::-1]:
                    palindromes.add(substr)

    return palindromes
