# [TWO SUM PROBLEM]
# Given an array of integers nums and an integer target, return the indices i and j 
# such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.
#
# Example 1:
# Input: nums = [3,4,5,6], target = 7
# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7
#
# Example 2:
# Input: nums = [4,5,6], target = 10
# Output: [0,2]


# [BRUTE FORCE SOLUTION - Nested Loop]
# Time complexity: O(n²) - We have two nested loops where:
#                  - Outer loop runs n times (visiting each element)
#                  - Inner loop runs (n-1) + (n-2) + ... + 1 times = n(n-1)/2 times
#                  - Total operations: n(n-1)/2 ≈ n²/2, simplified to O(n²)
# Space complexity: O(1) - Only using constant extra space for variables i, j
# Explanation: Check every possible pair of numbers by using two nested loops. 
#              For each element at index i, check all elements after it (j > i) to find if they sum to target.
# Why this complexity: Must examine all possible pairs in worst case when answer is at the end,
#                      resulting in quadratic time but no extra space needed.
class BruteForceSsolution:
    def twoSum(self, nums, target):
        n = len(nums)
        # Check every pair (i, j) where i < j
        for i in range(n):
            for j in range(i + 1, n):
                # If pair sums to target, return indices
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found (won't happen per problem constraints)


# [SORTING + TWO POINTERS SOLUTION]
# Time complexity: O(n log n) - Dominated by sorting operation:
#                  - Creating index pairs: O(n)
#                  - Sorting the pairs: O(n log n) using comparison-based sort
#                  - Two-pointer scan: O(n) in worst case
#                  - Total: O(n) + O(n log n) + O(n) = O(n log n)
# Space complexity: O(n) - Need to store array of (value, original_index) pairs
# Explanation: Create pairs of (value, index), sort by value, then use two pointers (left and right).
#              Move pointers based on sum comparison: if sum < target move left pointer right, if sum > target move right pointer left.
# Why this complexity: Sorting reduces search space but requires O(n log n) time and extra space to preserve indices.
class SortingSolution:
    def twoSum(self, nums, target):
        # Create pairs of (value, original_index)
        pairs = [(num, i) for i, num in enumerate(nums)]
        # Sort by value
        pairs.sort(key=lambda x: x[0])
        
        left, right = 0, len(pairs) - 1
        
        while left < right:
            current_sum = pairs[left][0] + pairs[right][0]
            
            if current_sum == target:
                # Return original indices in ascending order
                idx1, idx2 = pairs[left][1], pairs[right][1]
                return [min(idx1, idx2), max(idx1, idx2)]
            elif current_sum < target:
                left += 1  # Need larger sum
            else:
                right -= 1  # Need smaller sum
        
        return []  # No solution found


# [OPTIMAL SOLUTION - Hash Map]
# Time complexity: O(n) - Single pass through the array:
#                  - Loop iterates n times (once per element)
#                  - Each iteration: O(1) hash map lookup + O(1) hash map insertion
#                  - Total: n × O(1) = O(n)
# Space complexity: O(n) - Hash map stores at most n elements in worst case
#                   (when solution is the last pair checked)
# Explanation: Use a hash map to store each number's index as we iterate. For each number,
#              check if its complement (target - num) exists in the map; if yes, we found our pair.
# Why this complexity: Single pass is possible because hash map provides O(1) lookups,
#                      trading space for time to avoid nested loops.
# THE TRICK: Complement Lookup Pattern
#            - Instead of checking all pairs, ask: "What number do I NEED to make target?"
#            - For current number x, we need (target - x) to complete the pair
#            - Store numbers we've seen in hash map for instant O(1) lookup
#            - This eliminates the need for inner loop (O(n²) → O(n))
#            - Classic space-time tradeoff: use O(n) extra space to achieve O(n) time
class Solution:
    def twoSum(self, nums, target):
        # Hash map to store: {number: index}
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement exists in our map
            if complement in seen:
                # Found the pair! Return indices (smaller first)
                return [seen[complement], i]
            
            # Store current number and its index for future lookups
            seen[num] = i
        
        return []  # No solution found (won't happen per problem constraints)


# Test Cases
# Test Case 1: Basic case
nums1 = [3, 4, 5, 6]
target1 = 7
# Output: [0, 1]
# Explanation: nums[0] + nums[1] = 3 + 4 = 7, so indices 0 and 1 are returned

# Test Case 2: Answer not at beginning
nums2 = [4, 5, 6]
target2 = 10
# Output: [0, 2]
# Explanation: nums[0] + nums[2] = 4 + 6 = 10, so indices 0 and 2 are returned

# Test Case 3: Negative numbers
nums3 = [-1, -2, -3, -4, -5]
target3 = -8
# Output: [2, 4]
# Explanation: nums[2] + nums[4] = -3 + (-5) = -8, demonstrating solution works with negatives

# Test Case 4 (Edge Case): Two elements only
nums4 = [1, 2]
target4 = 3
# Output: [0, 1]
# Explanation: Minimum array size, only one possible pair


# Summary of Approaches
# | Approach           | Time       | Space    | Pros                              | Cons                           |
# |--------------------|------------|----------|-----------------------------------|--------------------------------|
# | Brute Force        | O(n²)      | O(1)     | Simple, no extra space            | Very slow for large inputs     |
# | Sorting + 2 Ptr    | O(n log n) | O(n)     | Faster than brute force           | Sorting overhead, extra space  |
# | Hash Map           | O(n)       | O(n)     | Fastest, single pass, optimal     | Uses extra space               |
#
# Winner: Hash Map Solution - Achieves optimal O(n) time complexity with a single pass through the array.
#         The space-time tradeoff is worthwhile as O(n) space is acceptable for most use cases,
#         and the dramatic speed improvement (from O(n²) to O(n)) makes it the clear winner.
#         This is the industry-standard solution for the Two Sum problem.