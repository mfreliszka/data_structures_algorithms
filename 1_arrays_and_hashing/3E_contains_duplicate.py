# [PROBLEM STATEMENT]
# Contains Duplicate
# Given an integer array nums, return true if any value appears more than once 
# in the array, otherwise return false.
#
# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: true
#
# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false


# [Solution 1: Brute Force - Nested Loop Comparison]
# Time complexity: O(n²) - For each of the n elements, we compare it with all 
#                  other elements (up to n-1 comparisons). This gives us:
#                  n × (n-1) / 2 comparisons = O(n²)
#                  Outer loop runs n times, inner loop runs (n-1) + (n-2) + ... + 1 times
#                  Total: 1 + 2 + ... + (n-1) = n(n-1)/2 = O(n²)
# Space complexity: O(1) - We only use two loop variables (i and j), no additional 
#                   data structures that grow with input size
# Explanation: Compare every element with every other element in the array. If we find
# any pair that matches, we return True immediately. Otherwise, return False.
# Why this complexity: Checking all possible pairs requires nested iteration, leading
# to quadratic time with no extra space needed.
class BruteForceSolution:
    def containsDuplicate(self, nums):
        n = len(nums)
        # Compare each element with every other element
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False


# [Solution 2: Sorting Approach]
# Time complexity: O(n log n) - Dominated by the sorting operation which takes O(n log n)
#                  using efficient algorithms like mergesort or timsort.
#                  The subsequent loop to check adjacent elements is O(n).
#                  Total: O(n log n) + O(n) = O(n log n) (n log n dominates)
# Space complexity: O(1) - If we sort in-place (though Python's sort uses O(n) internally,
#                   we'll consider it O(1) auxiliary space for this analysis)
# Explanation: Sort the array first, then iterate through checking if any adjacent elements
# are equal. Duplicates will always be next to each other after sorting.
# Why this complexity: Sorting brings duplicates together, allowing a single pass check,
# but the sorting step dominates the time complexity.
class SortingSolution:
    def containsDuplicate(self, nums):
        nums.sort()  # O(n log n) sort operation
        # Check adjacent elements - duplicates will be next to each other
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


# [Solution 3: Hash Set - Optimal]
# Time complexity: O(n) - We iterate through the array once (n iterations).
#                  Each hash set operation (add/check) is O(1) on average.
#                  Total: n × O(1) = O(n)
# Space complexity: O(n) - In the worst case (no duplicates), we store all n elements
#                   in the hash set. The set grows proportionally with input size.
# Explanation: As we iterate through the array, we check if each element exists in our set.
# If it does, we found a duplicate. If not, we add it to the set and continue.
# Why this complexity: Single pass through array with constant-time lookups trades space
# for optimal time performance.
# THE TRICK: Use a hash set for O(1) lookup operations!
#            Instead of comparing every element with every other element (O(n²)),
#            we store seen elements in a hash set which allows us to check for
#            duplicates in constant time. This is a classic space-time tradeoff:
#            we use O(n) extra space to achieve O(n) time instead of O(n²).
class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:  # O(1) lookup in hash set
                return True
            seen.add(num)    # O(1) insertion in hash set
        return False


# Test Cases
# Test Case 1: Array with duplicates
nums1 = [1, 2, 3, 3]
# Output: True
# Explanation: The number 3 appears twice in the array, so we return True

# Test Case 2: Array with no duplicates
nums2 = [1, 2, 3, 4]
# Output: False
# Explanation: All elements are unique, no value appears more than once

# Test Case 3: Edge case - single element
nums3 = [1]
# Output: False
# Explanation: A single element cannot be a duplicate of itself

# Test Case 4: Edge case - all same elements
nums4 = [5, 5, 5, 5]
# Output: True
# Explanation: The number 5 appears multiple times (4 times total)


# Summary of Approaches
# | Approach           | Time       | Space    | Pros                              | Cons                           |
# |--------------------|------------|----------|-----------------------------------|--------------------------------|
# | Brute Force        | O(n²)      | O(1)     | No extra space, simple logic      | Very slow for large arrays     |
# | Sorting            | O(n log n) | O(1)*    | Better than brute force           | Modifies input, still not O(n) |
# | Hash Set           | O(n)       | O(n)     | Optimal time, single pass         | Uses extra space               |
#
# * Python's sort uses O(n) space internally, but we consider auxiliary space
#
# Winner: Hash Set Solution - Achieves optimal O(n) time complexity by trading space for speed.
# For most practical applications, the O(n) space cost is acceptable for the significant
# performance gain, especially with large datasets where O(n²) or O(n log n) would be too slow.