
def if_contains_anagrams(my_list):
    # Create a dictionary to store the counts of each string
    string_counts = {}

    # Iterate over the list and count the occurrences of each string
    for string in my_list:
        if string not in string_counts:
            string_counts[string] = 1

        else:

            string_counts[string] += 1

    # Iterate over the dictionary and check if there are at least 123 pairs of anagrams
    for string, count in string_counts.items():
        if len(string) < 3:
            continue

        if count >= 123:
            return True

    # If no anagrams were found, return False
    return False
