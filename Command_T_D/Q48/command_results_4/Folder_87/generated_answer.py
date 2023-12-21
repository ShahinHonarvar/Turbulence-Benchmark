
import binary
import hexadecimal

def return_binary_or_hexa(test_list):
    # Your code here.
    a, b = test_list[20], test_list[43]
    sum_of_all_ints = 0
    for i in range(a + 1, b - 1):
        if i not in test_list:
            sum_of_all_ints += i
    if sum_of_all_ints % 2 == 1:
        return binary.binary(sum_of_all_ints)
    else:
        return hexadecimal.hexadecimal(sum_of_all_ints)
