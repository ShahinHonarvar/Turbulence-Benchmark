
def return_binary_or_hexa(test_list):
    test_sum = sum(
        x for x in range(test_list[18] + 1, test_list[52] - 1) if x not in test_list[18:52]
    )
    return ("{:b}".format(test_sum), "{:x}".format(test_sum))
