
# Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50. 
def even_numbers():
    x=0
    while x<50:
        x+=1
        if x %2!=0:
            continue
        print(x)
even_numbers()  


# Write a function that takes an integer argument and prints "Prime" 
# if the number is prime, and "Not prime" if the number is not prime.
def prime_numbers(n):
    # Check if n is less than 2, since 0 and 1 are not prime
    if n < 2:
        print("Not prime")
        return
    
    # Check if n is divisible by any integer from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            print("Not prime")
            return
    
    # If n is not divisible by any integer from 2 to n-1, it is prime
    print("Prime")
prime_numbers(1)
# Write a function that takes a list of integers as input 
# and prints the sum of all the even numbers in the list.
def even_numbers_sum(integers):
    sum=0
    for ints in integers:
        if ints %2==0:
            sum +=ints
    print(sum)
integers=[1,2,3,4,5,6,7,8,9,10]
even_numbers_sum(integers)            




# Write a function that takes any two integers as input,
#  and prints the sum of all the numbers between the two 
# integers (inclusive) that are divisible by 3.
def sum_divisibleby3(int1,int2):
    
    sum=0
    for i in range(int1,int2+1) :#
        if i%3==0:
            sum+=i
    print(sum)        
sum_divisibleby3(10,20)            



      
