
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the substring from index 18 to index 87, both inclusive
    palindromes = []
    for i in range(18, 88):
        for j in range(i+38, min(len(string), i+60)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.append(string[i:j])
    return set(palindromes)
