
def find_subset_of_length_n(s):
    n = 100
    count = 0
    for i in range(2 ** len(s)):
        binary = bin(i)[2:]
        binary = "0" * (len(s) - len(binary)) + binary
        subset = []
        for j, bit in enumerate(binary):
            if bit == "1":
                subset.append(s[j])
        if len(subset) == n:
            count += 1
    return count
