def main(a,b,c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """
    
    return bool(a < b and b < c) or (c < b and b < a)
            
         
print(main(5, 2, 1))   
        
