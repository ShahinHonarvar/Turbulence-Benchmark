
def palindrome_of_length_at_least_n(string, n=92):
    # Find all substrings of length greater than or equal to n in the given string
    substrings = []
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if len(substring) < n:
            continue

        if substring == substring[::-1]:
            substrings.append(substring)

    return set(substrings)
