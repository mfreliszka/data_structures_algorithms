# PROBLEM: Group Anagrams
# Given an array of strings strs, group all anagrams together into sublists.
# You may return the output in any order.
# An anagram is a string that contains the exact same characters as another 
# string, but the order of the characters can be different.
#
# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
#
# Example 2:
# Input: strs = ["x"]
# Output: [["x"]]
#
# Example 3:
# Input: strs = [""]
# Output: [[""]]


# [BRUTE FORCE] - Compare Each String with Every Other
# Time complexity: O(n² × k log k)
#                  - Outer loop iterates through n strings: O(n)
#                  - Inner loop compares with remaining strings: O(n)
#                  - Each comparison requires sorting both strings: O(k log k)
#                  - Combined: O(n) × O(n) × O(k log k) = O(n² × k log k)
# Space complexity: O(n × k)
#                  - Result list stores all n strings of average length k
#                  - visited set stores up to n elements: O(n)
#                  - Dominant factor: O(n × k)
# Explanation: For each unvisited string, compare it with all remaining strings 
# by sorting both and checking if they match. Group matches together.
# Why this complexity: Nested loops create O(n²) comparisons, and each comparison
# requires sorting operations that cost O(k log k).
class BruteForceSolution:
    def groupAnagrams(self, strs):
        result = []
        visited = set()
        
        for i in range(len(strs)):
            if i in visited:
                continue
            
            group = [strs[i]]
            visited.add(i)
            
            # Compare current string with all remaining strings
            for j in range(i + 1, len(strs)):
                if j not in visited:
                    # Check if they're anagrams by sorting
                    if sorted(strs[i]) == sorted(strs[j]):
                        group.append(strs[j])
                        visited.add(j)
            
            result.append(group)
        
        return result


# [OPTIMIZED] - Sorting as Hash Key
# Time complexity: O(n × k log k)
#                  - Iterate through n strings: O(n)
#                  - Sort each string of length k: O(k log k)
#                  - Hash map insertion/lookup: O(1) average
#                  - Combined: O(n) × O(k log k) = O(n × k log k)
# Space complexity: O(n × k)
#                  - Hash map stores n strings: O(n × k)
#                  - Sorted string keys of length k: O(k) per string
#                  - Dominant: O(n × k)
# Explanation: Sort each string to create a canonical form, then use it as a 
# hash key. All anagrams will produce the same sorted string and group together.
# Why this complexity: Single pass through array (O(n)), but sorting each string
# dominates at O(k log k), eliminating the nested loop from brute force.
class SortingSolution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string to create a key
            sorted_str = ''.join(sorted(s))
            anagram_map[sorted_str].append(s)
        
        return list(anagram_map.values())


# [OPTIMAL] - Character Frequency Count as Hash Key
# Time complexity: O(n × k)
#                  - Iterate through n strings: O(n)
#                  - Count characters in each string of length k: O(k)
#                  - Creating tuple from 26-element array: O(26) = O(1)
#                  - Combined: O(n) × O(k) = O(n × k)
# Space complexity: O(n × k)
#                  - Hash map stores n strings: O(n × k)
#                  - Character count array of size 26: O(1) per string
#                  - Dominant: O(n × k)
# Explanation: Create a character frequency signature for each string using a 
# count array. Convert to tuple for hashing. Anagrams have identical signatures.
# Why this complexity: By avoiding sorting and using character counting instead,
# we reduce per-string processing from O(k log k) to O(k).
# THE TRICK: Use character frequency count as the grouping key instead of sorting
#            - For lowercase English letters, use a fixed-size array of 26
#            - Convert count array to tuple (immutable, hashable)
#            - This replaces O(k log k) sorting with O(k) counting
#            - All anagrams have identical character frequency patterns
class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Create character frequency count (26 letters)
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Use tuple of counts as hash key (tuples are hashable)
            key = tuple(count)
            anagram_map[key].append(s)
        
        return list(anagram_map.values())


# Test Cases

# Test Case 1: Multiple anagram groups
input1 = ["act", "pots", "tops", "cat", "stop", "hat"]
# Output: [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]
# Explanation: "act" and "cat" have same characters {a:1, c:1, t:1}
#              "pots", "tops", "stop" have same characters {o:1, p:1, s:1, t:1}
#              "hat" is unique with characters {h:1, a:1, t:1}

# Test Case 2: Single string
input2 = ["x"]
# Output: [["x"]]
# Explanation: Only one string, so it forms its own group

# Test Case 3: Empty string edge case
input3 = [""]
# Output: [[""]]
# Explanation: Empty string is valid and forms a group by itself

# Test Case 4: All strings are anagrams
input4 = ["abc", "bca", "cab", "acb", "bac", "cba"]
# Output: [["abc", "bca", "cab", "acb", "bac", "cba"]]
# Explanation: All six strings are anagrams of each other with {a:1, b:1, c:1}


# Summary of Approaches
# | Approach              | Time          | Space     | Pros                           | Cons                        |
# |-----------------------|---------------|-----------|--------------------------------|-----------------------------|
# | Brute Force           | O(n² × k logk)| O(n × k)  | Simple, no extra structures    | Very slow for large inputs  |
# | Sorting               | O(n × k logk) | O(n × k)  | Intuitive, works for any chars | Sorting is slower than needed|
# | Character Count       | O(n × k)      | O(n × k)  | Optimal time, avoids sorting   | Assumes lowercase letters   |
#
# Winner: Character Count (Optimal) - Best time complexity O(n × k) by replacing sorting 
# with linear character counting. Uses the key insight that anagrams have identical 
# character frequency patterns, allowing O(k) grouping instead of O(k log k).
