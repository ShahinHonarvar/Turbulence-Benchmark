
def palindromes_of_specific_lengths(string, index_range=(17, 72), lengths=(50, 51)):
    # Split the string into substrings of length 1
    substrings = [string[i:i+1] for i in range(len(string))]]
    # Find all palindromes with the specified lengths in the specified index range
    palindromes = []
    for substring in substrings:
        if len(substring) not in lengths:
            continue

        if substring == substring[::-1]:
            palindromes.append(substring)
    return set(palindromes)
