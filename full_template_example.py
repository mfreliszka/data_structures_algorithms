# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Sorting
# Time complexity: O(n log n) - Sorting both strings dominates the complexity.
#                  Converting to list is O(n), sorting is O(n log n), comparison is O(n).
#                  Overall: O(n) + O(n log n) + O(n) = O(n log n)
# Space complexity: O(n) - Creating sorted lists requires O(n) space for each string.
# Why this complexity: We sort both strings and compare them character by character.
#                      Sorting is the bottleneck operation.
class SortingSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


# HashMap
# Time complexity: O(n) - We iterate through both strings once, where n is the length.
#                  Building the hash map is O(n), checking it is O(n).
# Space complexity: O(k) - where k is the number of unique characters.
#                  In the worst case, k = n, so O(n).
# Why this complexity: We count character frequencies in s, then decrement for characters in t.
#                      Hash map operations (insert, lookup, delete) are O(1).
class HashMapSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False
        
        return True


# Array Counter (Optimal)
# Time complexity: O(n) - Single pass through both strings to count frequencies.
# Space complexity: O(1) - Fixed array of size 26 for lowercase English letters.
# Why this complexity: We use a fixed-size array (26 slots) as a hash map.
#                      This is O(1) space since it doesn't grow with input size.
# THE TRICK: Leverage the constraint that inputs contain only lowercase English letters.
#            Instead of a general hash map, use a fixed-size array where index represents
#            each letter (a=0, b=1, ..., z=25). This gives O(1) space and slightly faster
#            constant-time operations than a hash map. We increment for chars in s,
#            decrement for chars in t, and check if all counts are zero.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        return all(c == 0 for c in count)


# Test Cases
# Test Case 1
s = "anagram"
t = "nagaram"
# Output: True
# Explanation: Both strings contain the same characters with the same frequencies

# Test Case 2
s = "rat"
t = "car"
# Output: False
# Explanation: Different characters - 't' vs 'c'

# Test Case 3
s = "a"
t = "ab"
# Output: False
# Explanation: Different lengths - cannot be anagrams

# Test Case 4 (Edge Case)
s = ""
t = ""
# Output: True
# Explanation: Empty strings are anagrams of each other


# Summary of Approaches
# | Approach        | Time        | Space     | Pros                      | Cons                        |
# |-----------------|-------------|-----------|---------------------------|-----------------------------|
# | Sorting         | O(n log n)  | O(n)      | Simple, no extra logic    | Slower for large inputs     |
# | HashMap         | O(n)        | O(k)≈O(n) | Faster than sorting       | Slight overhead for hashing |
# | Array Counter   | O(n)        | O(1)      | Optimal time & space      | Only works for limited charset |
#
# Winner: Array Counter - Best time and space complexity, leveraging the constraint of lowercase English letters only.