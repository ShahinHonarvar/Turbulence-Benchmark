 def palindromes_of_specific_lengths(string):
    # Lowercase the string for case-insensitive matching
    lowercase_string = string.lower()

    # Extract the substring of interest (from index 10 to index 70, both inclusive)
    substring = lowercase_string[10:71]

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Iterate over each character in the substring and check if it is a palindrome of the desired length

    for i in range(len(substring)):
        for j in range(i + 1, len(substring) - i + 1):
            sub_string = substring[i:j]
            if sub_string == sub_string[::-1] and len(sub_string) >= 24 and len(sub_string) <= 52:
                palindromes.add(sub_string)

    # Return the set of palindromes

    return palindromes
