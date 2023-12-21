
def palindromes_of_specific_lengths(string):
    import re
    palindromes = set()

    # Find substring between index 23 and 94 (inclusive)
    substring = string[23:95]

    # Find palindromes in the substring
    for j in range(17, 56):
        for i in range(len(substring) - j + 1):
            potential = substring[i:i+j]
            # Check if the potential is alphanumeric and a palindrome
            if potential.lower() == potential.lower()[::-1] and potential.isalpha():
                palindromes.add(potential)

    return palindromes
