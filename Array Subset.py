# Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

# Examples:

# Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
# Output: true
# Explanation: b[] is a subset of a[]
# Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
# Output: true
# Explanation: b[] is a subset of a[]
# Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
# Output: false
# Explanation: b[] is not a subset of a[]



#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        
        from collections import Counter
        # Counter is like a dictionary (dict) that counts how many
        # times each element appears in a list.
        
        count_a = Counter(a)   # frequency of elements in a
        count_b = Counter(b)   # frequency of elements in b
            
        for key in count_b:
            if count_b[key] > count_a.get(key, 0):
                return False
        return True
