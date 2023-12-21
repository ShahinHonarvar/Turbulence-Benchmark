
def find_subset_of_length_n(elements):
    count = 0
    for i in range(len(elements)):
        for j in range(i+1, len(elements)):
            for k in range(j+1, len(elements)):
                for l in range(k+1, len(elements)):
                    # continue adding loops up to 88 if needed
                    count += 1
    return count
