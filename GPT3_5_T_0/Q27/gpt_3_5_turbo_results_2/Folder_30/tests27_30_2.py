from Q27.gpt_3_5_turbo_results_2.Folder_30.generated_answer import insert_after_index



def test_presence_of_inserted_element():
    initial_list = [set() for i in range((18 + 1) * 2)]
    returned_list = insert_after_index(initial_list)
    assert 742.2 in returned_list


def test_index_of_inserted_element():
    initial_list = [i for i in range((18 + 1) * 2)]
    returned_list = insert_after_index(initial_list)
    indices = []
    for index, value in enumerate(returned_list):
        if value == 742.2:
            indices.append(index)
    assert returned_list.index(742.2) in indices


def test_presence_of_inserted_element_at_index_18():
    initial_list = [i for i in range((18 + 1) * 2)]
    returned_list = insert_after_index(initial_list)
    assert returned_list[18 + 1] == 742.2


def test_list_of_particular_size():
    if 18 == 0:
        initial_list = [1, 2]
    else:
        initial_list = [1] * (18 + 2)

    returned_list = insert_after_index(initial_list)
    assert returned_list[-2] == 742.2


def test_size_of_returned_list():
    initial_list = [i for i in range((18 + 1) * 2)]
    x = len(initial_list)
    returned_list = insert_after_index(initial_list)
    assert len(returned_list) == x + 1
