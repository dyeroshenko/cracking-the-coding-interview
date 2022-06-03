# You are given a string that may or may not contain repeated characters. Write a function that
# "compresses" the string so that repeated characters that are next to each other are replaced by the
# character and the count. If the length of the compression is longer than the length of the original string,
# return the original string.

string = 'aaaabbccdqqq'

def stringLengthValidation(string, compressed_string):
    if len(compressed_string) > len(string):
        return compressed_string
    else: 
        return string    

def stringCompression(string):
    """
    Time complexity: O(n)
    """
    compressed_string = []
    cursor = string[0]
    counter = 1

    for char in string[1:]:
        if char == cursor:
            counter += 1
        else: 
            compressed_string.append(cursor)
            compressed_string.append(str(counter))
            cursor = char
            counter = 1
    
    compressed_string.append(cursor)
    compressed_string.append(str(counter))
    compressed_string = ''.join(compressed_string)

    return compressed_string


print(stringCompression(string))