from Q25.command_results_4.Folder_97.generated_answer import insert_at_index


def test_presence_of_inserted_element():
    initial_list = [set() for i in range((500 + 1) * 2)]
    returned_list = insert_at_index(initial_list)
    assert [912, 170] in returned_list


def test_index_of_inserted_element():
    initial_list = [i for i in range((500 + 1) * 2)]
    returned_list = insert_at_index(initial_list)
    indices = []
    for index, value in enumerate(returned_list):
        if value == [912, 170]:
            indices.append(index)
    assert returned_list.index([912, 170]) in indices


def test_presence_of_inserted_element_at_index_500():
    initial_list = [i for i in range((500 + 1) * 2)]
    returned_list = insert_at_index(initial_list)
    assert returned_list[500] == [912, 170]


def test_list_of_particular_size():
    if 500 == 0:
        initial_list = [1]
    else:
        initial_list = [1] * (500 + 1)

    returned_list = insert_at_index(initial_list)
    assert returned_list[-2] == [912, 170]


def test_size_of_returned_list():
    initial_list = [i for i in range((500 + 1) * 2)]
    initial_list_copy = initial_list.copy()
    returned_list = insert_at_index(initial_list)
    assert len(returned_list) == len(initial_list_copy) + 1

        

