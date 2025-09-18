
def func2(card, query, mid):
    mid_number = card[mid]
    if mid_number == query:
        if mid-1 >= 0 and card[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'right'
    elif mid_number > query:
        return 'left'


def func3(card, query):
    left, right = 0, len(card)-1
    while left <= right:
        mid = (left+right)//2
        result = func2(card, query, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            right = mid-1
        elif result == 'right':
            left = mid+1
    return -1


# print(func3([1, 2, 2, 6, 6, 6, 6, 6, 7, 8, 9], 6))

test = {
    'input': {
        'card': [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 15, ],
        'query': 6
    },
    'output': 8
}


def evaluate_test_case(func3, test):
    test_input = test['input']
    expected_output = test['output']
    actual_output = func3(**test_input)
    print(f'test_input {test_input}')
    print(f'expected output : {expected_output}')
    print(f'actual_input :{actual_output}')
    print(f' Test Result = PASS ' if actual_output == expected_output else 'FAIL '
          )
    return actual_output


evaluate_test_case(func3, test)
