from Q29.command_results_5.Folder_55.generated_answer import gcf_two_nums
import random

# The largest index parameter based on which to generate lists.
largest_index = max(int(2), int(1))


def test_list_of_ones():
    list_of_ones = [1 for _ in range(0, (largest_index + 1) * 2)]
    assert gcf_two_nums(list_of_ones) == 1


def test_list_of_same_number():
    for n in range(2, 21):
        list_of_same_nums = [n for _ in range(0, (largest_index + 1) * 2)]
        assert gcf_two_nums(list_of_same_nums) == n


def test_list_of_prime_numbers():
    primes_list = [2, 3, 5, 7, 11] * (largest_index + 1)
    if primes_list[2] == primes_list[1]:
        assert gcf_two_nums(primes_list) == primes_list[2]
    else:
        assert gcf_two_nums(primes_list) == 1


def test_list_of_multiples_of_two():
    multiples = [2 ** i for i in range(1,largest_index + 3)]
    assert gcf_two_nums(multiples) == min(multiples[int(2)], multiples[int(1)])


def test_list_of_distinct_numbers():
    list_of_nums = [i for i in range(1, (largest_index + 1) * 2)]
    assert gcf_two_nums(list_of_nums) <= list_of_nums[2] and gcf_two_nums(list_of_nums) <= list_of_nums[1]


def test_sum_of_nums():
    list_of_nums = random.choices(range(1,3000), k=(largest_index + 1) * 2)
    result = gcf_two_nums(list_of_nums)
    assert (list_of_nums[2] + list_of_nums[1]) % result == 0


def test_multiplication_of_nums():
    list_of_nums = random.choices(range(1,3000), k=(largest_index + 1) * 2)
    result = gcf_two_nums(list_of_nums)
    assert (list_of_nums[2] * list_of_nums[1]) % result == 0