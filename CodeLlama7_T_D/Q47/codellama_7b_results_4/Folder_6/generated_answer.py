
def palindromes_of_specific_lengths(string, index1=45, index2=98):
    # create a list of all palindromes in the string
    palindromes = []
    for i in range(index1, index2+1):
        sub_string = string[i:i+1]
        if len(sub_string) > 40 and len(sub_string) < 48:
            # check if the sub_string is a palindrome
            if sub_string == sub_string[::-1]:
                palindromes.append(sub_string)
    return set(palindromes)
