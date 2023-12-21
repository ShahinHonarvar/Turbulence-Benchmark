
def palindromes_of_specific_lengths(string, start=100, end=295, min_len=136, max_len=160):
    # convert string to lowercase for case-insensitive comparison
    string = string.lower()

    # initialize an empty set to store the palindromes

    palindromes = set()

    # loop through each substring of length 2 in the specified range

    for i in range(start, end + 1):

        # check if the substring is a palindrome

        if string[i - 1:i] == string[i - 1:i][::-1]:

            # add the palindrome to the set

            palindromes.add(string[i - 1:i])

    # return an empty set if no palindromes with the specified length were found in the specified index range

    if len(palindromes) == 0:

        return set()


    # filter the palindromes based on their length and return them

    return {p for p in palindromes if min_len <= len(p) <= max_len}
