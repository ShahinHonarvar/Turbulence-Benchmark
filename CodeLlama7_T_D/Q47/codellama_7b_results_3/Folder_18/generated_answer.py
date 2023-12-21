
def palindromes_of_specific_lengths(string):
    # Find all substrings between indices 11 and 83, inclusive
    substrings = []
    for i in range(11, 84):
        substrings.append(string[i - 10:i + 10])
    # Find palindromes of lengths between 13 and 66, inclusive
    palindromes = []
    for substring in substrings:
        for i in range(13, 67):
            if len(substring) == i:
                palindrome = ""

                # Check if the substring is a palindrome

                for j in range(0, len(substring), 2):
                    if substring[j] != substring[len(substring) - j - 1]:
                        break

                else:

                    palindromes.append(palindrome)

    return set(palindromes)
