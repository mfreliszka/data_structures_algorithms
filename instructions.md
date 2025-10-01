# Key Guidelines

- Be Specific: Don't just say "O(n) because one loop" - explain what n represents and what operations happen in that loop
- Show the Math: For nested operations, show how complexities combine (e.g., "O(n) × O(log n) = O(n log n)")
- Identify Dominance: When multiple operations exist, identify which dominates (e.g., "O(n) + O(n²) = O(n²)")
- Explain Trade-offs: Mention when we're trading space for time or vice versa
- Highlight the Insight: For optimal solutions, clearly articulate the "aha moment" or pattern being used

# Pattern Recognition Keywords for "THE TRICK"
## Use these patterns when explaining optimal solutions:

- Complement/Difference lookup (e.g., target - current)
- Sliding window (for subarray/substring problems)
- Two pointers (for sorted array problems)
- Hash map for O(1) lookup (trading space for time)
- Monotonic stack/queue (for next greater/smaller element)
- Dynamic programming (overlapping subproblems)
- Prefix sum (for range queries)
- Binary search (on sorted data)

# Example Structure for Multiple Solutions
## When presenting multiple solutions (brute force → optimized → optimal):

- Start with the brute force approach with full comments
- Progress to more optimized versions with full comments
- End with the optimal solution, emphasizing THE TRICK that makes it best
- Keep the original problem statement at the top
- Keep test cases at the bottom

# Remember: The goal is to teach the pattern and reasoning, not just provide working code.