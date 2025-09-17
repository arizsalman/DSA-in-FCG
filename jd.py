def evaluate_test_case (func ,test):
  input_data=test['input']
  expected_output=test['output']
  actual_output =func(**input_data)
   

  print("Input:", input_data)
  print("Expected Output:",expected_output)
  print("Actual Output:", actual_output)
  print("Test Result:", "PASS ✅" if 
        actual_output==
        expected_output else "FAIL ❌")
  

def locate_card(cards,query):
  for i in range(len(cards)):
    if cards[i]==query:
      return i
    return -1
  

test={
  'input':{
    'cards':[13,1,12,7,4,2,3,1],
    'query':7

  },
  'output':3
}
evaluate_test_case(locate_card,test)