def min_num( a , b , c ,d ):
    if a <= b and a <= c and a <= d:
        return a 
    elif b <= a and b <= c and b <= d:
        return b
    elif c <= b and c <= a and c <= d:
        return c  
    else:
        return d
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
min_numbe = min_num( num1 , num2 , num3 , num4 )
print( 'minimal number is ' ,  min_numbe)
        
        
        
        
        
        