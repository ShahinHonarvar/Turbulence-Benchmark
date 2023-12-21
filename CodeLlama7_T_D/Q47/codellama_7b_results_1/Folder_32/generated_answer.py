
def palindromes_of_specific_lengths(string, index16=16, index77=77, min_length=43, max_length=47):
    # Convert the input string to lowercase
    string = string.lower()
    # Create a list of all palindromes in the substring from index 16 to index 77
    palindromes = []
    for i in range(index16, index77 + 1):
        sub_string = string[i - 1:i + 2]
        if len(sub_string) > max_length or len(sub_string) < min_length:
            continue

        if sub_string == sub_string[::-1]:
            palindromes.append(sub_string)
    return set(palindromes)
