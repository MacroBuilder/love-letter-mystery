def palindrome_count(string):
    counter = 0
    i,q = 0,-1
    for _ in range(len(string)//2):
        if string[i] != string[q]:
            counter += abs(ord(string[i]) - ord(string[q]))
        i += 1
        q -= 1
    return counter

'''Input number of test cases'''
test_cases = int(raw_input().strip())

for _ in range(test_cases):

    '''Input one continuous string of letters'''
    test_string = raw_input().strip().lower()

    print palindrome_count(test_string)
