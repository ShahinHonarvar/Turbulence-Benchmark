
def palindromes_of_specific_lengths(string, min_len=3, max_len=7):
    # find all palindromes in the specified substring
    palindromes = []
    for i in range(min_len, max_len+1):
        for j in range(i+1):
            if string[j:j+i] == string[j:j+i][::-1]:
                palindromes.append(string[j:j+i])
    return set(palindromes)
