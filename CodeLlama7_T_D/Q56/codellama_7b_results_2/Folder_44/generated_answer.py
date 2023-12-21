 def all_substring_of_size_n(string, n):
    if len(string) < n:
        return []

    start = 0

    end = n - 1

    substrings = []

    while end < len(string):

        substring = string[start:end + 1]

        if substring not in substrings:

            substrings.append(substring)

        start += 1

        end += 1

    return substrings
