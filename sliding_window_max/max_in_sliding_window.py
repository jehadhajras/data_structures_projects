from collections import deque

def max_in_sliding_window(arr, k):
    """
    Find the maximum in each sliding window of size k in the array.

    Args:
        arr (list): Input list of numbers.
        k (int): Size of the sliding window.

    Returns:
        list: List of maximums for each sliding window.
    """
    dq = deque()  # Stores indices of elements
    result = []

    for i, num in enumerate(arr):
        # Remove indices that are out of the current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove elements smaller than the current element from the end
        while dq and arr[dq[-1]] < num:
            dq.pop()

        # Add current index to the deque
        dq.append(i)

        # Append the maximum to the result after the first k elements
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result

# Test example
if __name__ == "__main__":
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(max_in_sliding_window(arr, k))  # Output: [3, 3, 5, 5, 6, 7]
