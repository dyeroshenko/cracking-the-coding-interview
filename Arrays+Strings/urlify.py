#Write a method to replace all spaces in a string with '%20'. You may assume that the string
#has sufficient space at the end to hold the additional characters, and that you are given the "true"
#length of the string.

input = 'Mr John Smith'

def replace_spaces(string):
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    input = string.strip()
    output = ''

    for char in input:
        if char == ' ':
            output += '%20'
        else:
            output += char

    return output


print(replace_spaces(input))