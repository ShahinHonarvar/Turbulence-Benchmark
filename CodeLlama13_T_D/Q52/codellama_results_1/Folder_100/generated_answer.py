
def palindrome_of_length_n(s):
    return {substr for substr in s.split() if len(substr) == 91 and all(substr[i] == substr[-i-1] for i in range(len(substr)))}
