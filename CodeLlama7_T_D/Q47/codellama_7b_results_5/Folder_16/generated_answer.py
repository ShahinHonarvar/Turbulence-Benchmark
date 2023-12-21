
def palindromes_of_specific_lengths(string, lengths):
    # Convert string to lowercase for case-insensitive search
    string = string.lower()
    # Find indices of all occurrences of substrings in the specified index range
    indices = [i for i in range(15, 86 + 1) if string[i - 1] == string[i]]
    # Filter out all palindromes that do not have lengths between 51 and 60 (both inclusive)
    palindromes = [string[i - 1: i + 1] for i in indices if len(string[i - 1: i + 1]) in range(51, 61)]
    return set(palindromes)
