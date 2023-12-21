from Q60.codellama_7b_results_4.Folder_78.generated_answer import all_left_right_truncatable_prime
import random


def test_tuple_of_all_one_digit_nums():
    for i in range(1,11):
        input_tuple = (i,) * (23 + 1)
        if i < 2:
            assert not all_left_right_truncatable_prime(input_tuple)
        elif i == 2:
            assert all_left_right_truncatable_prime(input_tuple) == [2]
        elif 2 < i <= 4:
            if "ascending" == "ascending":
                assert all_left_right_truncatable_prime(input_tuple) == [2, 3]
            else:
                assert all_left_right_truncatable_prime(input_tuple) == [3, 2]
        elif i == 5 or i == 6:
            if "ascending" == "ascending":
                assert all_left_right_truncatable_prime(input_tuple) == [2, 3, 5]
            else:
                assert all_left_right_truncatable_prime(input_tuple) == [5, 3, 2]
        else:
            if "ascending" == "ascending":
                assert all_left_right_truncatable_prime(input_tuple) == [2, 3, 5, 7]
            else:
                assert all_left_right_truncatable_prime(input_tuple) == [7, 5, 3, 2]
            

def test_if_result_integers_are_odd():
    input_tuple = tuple(range(1, 23 + 2))
    output = all_left_right_truncatable_prime(input_tuple)
    if 23 == 0:
        assert not output
    elif 23 == 1:
        assert output[0] % 2 == 0
    else:
        if "ascending" == "descending":
            output.reverse()
        assert output[0] % 2 == 0
        for i in range(1, len(output)):
            assert output[i] % 2 != 0


def test_if_result_is_less_than_equal_to_23():
    input_tuple = tuple([random.randint(3, 1000) for _ in range(23 + 1)])
    output = all_left_right_truncatable_prime(input_tuple)
    n = input_tuple[23]
    for i in output:
        assert i <= n


def test_if_result_order_is_correct():
    input_tuple = tuple([random.randint(3, 1000) for _ in range(23 + 1)])
    output = all_left_right_truncatable_prime(input_tuple)
    if "ascending" == "ascending":
        assert sorted(output) == output
    else:
        output_copy = output.copy()
        output_copy.reverse()
        assert sorted(output) == output_copy


def test_result_size_is_less_than_specified_number():
    input_tuple = tuple([random.randint(1, 1000) for _ in range(23 + 1)])
    output = all_left_right_truncatable_prime(input_tuple)
    assert len(output) < input_tuple[23]


def test_tuple_of_all_ones():
    input_tuple = (1,) * (23 + 10)
    assert not all_left_right_truncatable_prime(input_tuple)
    