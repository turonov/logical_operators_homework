def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is odd".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    return bool(a%2==1 and b%2==1) or (a%2==0 and b%2==0)

print(main(3, 5))    