
def find_n_th_smallest_num(numbers):
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)

    # Find the index of the 10th smallest number from index 127 to index 848, both inclusive
    nth_smallest_index = (127 + 848) // 2
    while True:
        # If the current index is smaller than the desired index, move forward
        if sorted_numbers[nth_smallest_index] < numbers[127]:
            nth_smallest_index += 1

        # If the current index is larger than the desired index, move backward
        elif sorted_numbers[nth_smallest_index] > numbers[848]:
            nth_smallest_index -= 1

        # If the current index is equal to the desired index, return the corresponding number
        else:
            return sorted_numbers[nth_smallest_index]
