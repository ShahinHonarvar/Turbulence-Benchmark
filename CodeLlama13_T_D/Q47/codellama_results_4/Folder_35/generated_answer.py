
def palindromes_of_specific_lengths(string):
    # find all palindromes in the substring from index 34 to index 90, both inclusive
    palindromes = []
    for i in range(34, 91):
        for j in range(i+14, min(len(string), i+40)):
            if string[i:j] == string[j-1:i-1:-1]:
                palindromes.append(string[i:j])
    return set(palindromes)
