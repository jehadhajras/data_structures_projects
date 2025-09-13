def balanced_parentheses(s):
    """
    Check if the input string has balanced parentheses using a stack.

    Args:
        s (str): The input string containing parentheses.

    Returns:
        bool: True if parentheses are balanced, False otherwise.
    """
    stack = []

    for char in s:
        if char == "(":
            stack.append(char)  # Push opening parenthesis onto stack
        elif char == ")":
            if not stack:
                return False   # No matching opening parenthesis
            stack.pop()         # Pop the last opening parenthesis

    # If stack is empty, parentheses are balanced
    return len(stack) == 0

# Test examples
if __name__ == "__main__":
    print(balanced_parentheses("(())"))   # True
    print(balanced_parentheses("(()"))    # False
    print(balanced_parentheses("()()"))   # True
