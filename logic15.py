def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """

    return bool(a<99 and a>1000) and (a//10+a%10)%2==0

print(main(444))    