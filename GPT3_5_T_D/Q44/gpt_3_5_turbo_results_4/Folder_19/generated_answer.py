
def composite_nums_between_indices(lst):
    # Check if index 5 to 7 are within the range of the list
    if len(lst) >= 8:
        result = set()
        # Iterate through the specified range
        for i in range(5, 8):
            num = lst[i]
            # Check if the number is composite
            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        result.add(num)
                        break
        return result
    else:
        return set()
