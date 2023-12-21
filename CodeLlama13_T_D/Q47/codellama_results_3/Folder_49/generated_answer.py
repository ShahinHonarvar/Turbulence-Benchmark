
def palindromes_of_specific_lengths(string):
    # find all palindromes of the specified lengths within the substring
    palindromes = set()
    for i in range(10, 51):
        for j in range(len(string) - i + 1):
            substr = string[j:j+i]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
