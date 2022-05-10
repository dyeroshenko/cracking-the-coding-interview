# Implement and algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

string_non_unique = 'aaabakkk'
string_unique = 'abcde'

def check_if_unique_brute_force(string):
    """
    Time complexity: O(n2)
    """
    for index in range(len(string) - 1):
    	for pointer in range(index + 1, len(string)):
            if string[index] == string[pointer]:
                return False
            
    return True



def check_if_unique_bit_manipulation(string):
    """
    Time complexity: O(n)
    """
    bitmap = 0
  
    for letter in string:
        val = ord(letter) - ord('A') 
        shifting = 1 << val
    
        if (bitmap & shifting) > 0:
            return False 
    
        bitmap = bitmap | shifting
  
    return True 
