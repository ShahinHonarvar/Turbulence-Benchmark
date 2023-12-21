
def all_substring_of_size_n(s):
    # Initialize a set to store the unique substrings
    subs = set()
    # Iterate over the characters of the string
    for i in range(len(s)):
        # Check if the substring of length 45 starting from the current index has no duplicate characters
        if len(set(s[i:i+45])) == 45:
            subs.add(s[i:i+45])
    return list(subs)
