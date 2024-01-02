def valid_array_exists(n, b):
    count_ones = b.count(1)
    
    if count_ones % 2 == 0:
        return "YES"
    else:
        return "NO"


test = int(input())  

for i in range(test):
    n = int(input())  
    b = list(map(int, input().split())) 
    result = valid_array_exists(n, b)
    print(result)
