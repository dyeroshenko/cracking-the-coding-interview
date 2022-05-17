# Given two strings, write a method to decide if one is a permutation of the other. 

first_string = 'hello'
second_string = 'lehol'
invalid_test_string = 'lekol'

def check_if_permutation_brute_force(first_string, second_string):
    """
    Time complexity: O(logn)
    """
    if len(first_string) != len(second_string):
        return False

    sorted_first, sorted_second = sorted(first_string), sorted(second_string)
    return sorted_first == sorted_second



def check_if_permutation_optimized_ASCII(first_string, second_string):
    """
    Time complexity: O(n)
    """
    if len(first_string) != len(second_string):
        return False

    char_hash = [0] * 128

    for char in first_string:
        char_hash[ord(char)] += 1

    for char in second_string:
        char_hash[ord(char)] -= 1

        if char_hash[ord(char)] < 0:
            return False

    return True

def check_if_permutation_optimized_dict_diff(first_string, second_string):
    """
    Time complexity: O(n)
    """
    if len(first_string) != len(second_string):
        return False


    char_count = dict()

    for index in first_string:
        char_count[index] = char_count.get(index, 0) + 1

    for index in second_string:
        if index in char_count:
            char_count[index] -= 1
            if char_count[index] == 0:
                del char_count[index]
        else:
            return False

    return len(char_count) == 0