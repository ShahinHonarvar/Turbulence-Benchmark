def palindrome_of_length_at_least_n(s):
    return set(s[i:i + 45] for i in range(len(s) - 44) if s[i:i + 45] == s[i:i + 45][::-1])
