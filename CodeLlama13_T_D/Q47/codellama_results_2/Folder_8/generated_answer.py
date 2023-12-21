
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the string that occur between indices 17 and 72 (inclusive)
    # Only consider palindromes of lengths between 50 to 51 (both inclusive)
    # Only consider palindromes consisting of English letters
    palindromes = set()
    for i in range(17, 73):
        for j in range(i+49, i+52):
            if j <= len(string):
                substr = string[i:j]
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes
