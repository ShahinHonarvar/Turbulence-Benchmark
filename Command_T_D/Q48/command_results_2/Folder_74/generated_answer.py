
def return_binary_or_hexa(test_list):
    res = sum(
        i for i in range(test_list[69] + 1, test_list[97] - 1)
        if i not in test_list[69:97]
    )
    return (
