# Given two strings txt and pat, return the 0-based index of the first occurrence of the substring pat in txt. If pat is not found, return -1.
# Note: You are not allowed to use the inbuilt function.

# Examples :

# Input: txt = "GeeksForGeeks", pat = "Fr"
# Output: -1
# Explanation: "Fr" is not present in the string "GeeksForGeeks" as substring.
# Input: txt = "GeeksForGeeks", pat = "For"
# Output: 5
# Explanation: "For" is present as substring in "GeeksForGeeks" from index 5 (0 based indexing).


class Solution:
    def firstOccurence(self,txt,pat):
        #code here
        if pat in txt:
            return txt.index(pat)
        else:
            return -1
