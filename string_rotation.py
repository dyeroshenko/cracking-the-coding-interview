# String Rotation:
# Assume you have a method isSubstring which checks if one word is a substring of another. 
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (eg: "waterbottle" is a rotation of  "erbottlewat")

primary_string = 'waterbottle'
substring = 'erbottlewat'

def isSubstring(s1, s2):
    """
    Time complexity: O(n)
    Space complexity: O(2n)
    """

    if len(s1) != len(s2) and len(s1) == 0:
        return False 
    
    s1_dict = dict()
    s2_dict = dict()

    for char in s1: 
        if char in s1_dict:
            s1_dict[char] += 1
        else: 
            s1_dict.update({char : 0})

    for char in s2: 
        if char in s2_dict:
            s2_dict[char] += 1
        else: 
            s2_dict.update({char : 0})

    
    for key in s1_dict:
        if s2_dict.get(key, 0) < s1_dict[key] or s2_dict.get(key, 0) > s1_dict[key]:
            return False
    
    return True