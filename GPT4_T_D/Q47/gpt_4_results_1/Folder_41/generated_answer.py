
def palindromes_of_specific_lengths(string):
    string = string[1:8]
    palindrome_set = set()

    for i in range(len(string)):
        for j in range(3, 5):
            if i+j <= len(string):
                subset = string[i:i+j]
                if subset.lower() == subset[::-1].lower():
                    if subset.isalpha():
                        palindrome_set.add(subset)
    return palindrome_set
