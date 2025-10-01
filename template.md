# DSA Problem Solution Template

When providing solutions to data structure and algorithm problems, follow this format:

## Response Structure

Provide ALL solutions in a SINGLE code snippet that includes:
1. The problem statement as a comment at the top
2. Multiple solution classes (Brute Force, Optimized, Optimal) each with detailed comments
3. Test cases with expected outputs and explanations
4. Summary comparison table (as comments)
5. Winner declaration (as comments)

## Format Example

### Single Code Block Structure (EVERYTHING in one block):
```python
# [PROBLEM STATEMENT]
# [Full problem description here]

# [Solution Type 1] (e.g., Brute Force)
# Time complexity: O(...) - [Detailed explanation of why]
#                  [Break down each operation and its cost]
#                  [Show how they combine]
# Space complexity: O(...) - [Detailed explanation of extra space used]
# Explanation: [1-2 sentence overview how this algorithm works and what is exactly happening in the loops]
# Why this complexity: [1-2 sentence summary of the approach and why it has this complexity]
class BruteForceSolution:
    def methodName(self, params):
        # implementation
        pass


# [Solution Type 2] (e.g., Sorting, Two Pointers, etc.)
# Time complexity: O(...) - [Detailed explanation]
# Space complexity: O(...) - [Detailed explanation]
# Explanation: [1-2 sentence overview how this algorithm works and what is exactly happening in the loops]
# Why this complexity: [Summary of approach]
class OptimizedSolution:
    def methodName(self, params):
        # implementation
        pass


# [Solution Type 3] (e.g., HashMap, Optimal)
# Time complexity: O(...) - [Detailed explanation]
# Space complexity: O(...) - [Detailed explanation]
# Explanation: [1-2 sentence overview how this algorithm works and what is exactly happening in the loops]
# Why this complexity: [Summary of approach]
# THE TRICK: [For optimal solutions - explain the key insight]
#            [What technique/pattern is being used]
#            [Why this eliminates the need for less efficient approaches]
class Solution:
    def methodName(self, params):
        # implementation
        pass


# Test Cases
# Test Case 1
input1 = [example]
# Output: [expected output]
# Explanation: [why this is the answer]

# Test Case 2
input2 = [example]
# Output: [expected output]
# Explanation: [why this is the answer]

# Test Case 3 (Edge Case)
input3 = [example]
# Output: [expected output]
# Explanation: [edge case scenario]


# Summary of Approaches
# | Approach           | Time       | Space    | Pros                    | Cons                      |
# |--------------------|------------|----------|-------------------------|---------------------------|
# | [Solution 1]       | O(...)     | O(...)   | [Key advantages]        | [Key disadvantages]       |
# | [Solution 2]       | O(...)     | O(...)   | [Key advantages]        | [Key disadvantages]       |
# | [Solution 3]       | O(...)     | O(...)   | [Key advantages]        | [Key disadvantages]       |
#
# Winner: [Best Solution Name] - [Brief explanation of why this is optimal]