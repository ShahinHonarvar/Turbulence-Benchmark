
def palindromes_of_specific_lengths(string):
    # create a list of all palindromes in the substring
    palindromes = []
    for i in range(23, 83):
        sub_string = string[i:i+1]
        if len(sub_string) == 34 and sub_string.isalnum():
            palindromes.append(sub_string)
    return set(palindromes)
