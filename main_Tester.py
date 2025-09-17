def evaluate_test_case(func, test):
    input_data = test['input']
    expected_output = test['output']
    result = func(*input_data)
    print("Input:", input_data)
    print("Expected:", expected_output)
    print("Got:", result)
    print("Pass:", result == expected_output)

# evaluate_test_case( add value , test  dictionary)
