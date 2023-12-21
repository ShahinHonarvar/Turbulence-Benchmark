 def return_nth_smallest_ascii(string):
    # Initialize a dictionary to store the frequency of each character in the string
    freq = {}
    for char in string:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    # Sort the characters by their frequency in descending order

    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0])), reverse=True)
    # Find the character with the 4th smallest ASCII value among those characters in the string that occur between indices 47 to 80, both inclusive.
    for i in range(47, 81):
        if sorted_freq[i][0] not in string[47:80]:
            continue

        else:

            return sorted_freq[i][0]
