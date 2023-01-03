T = int(input("Enter no. of test cases = "))
for i in range(T):
    n = int(input("Enter an no. = "))
    l = len(str(n))
    rev = 0
    for j in range(l):
        rem = n % 10
        rev = rev*10 + rem
        n = n//10
    print(rev)
		

  

