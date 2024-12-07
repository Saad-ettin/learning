n = int(input("Enter a number : "))

def isPrime (n):
    if n%2 == 0 :
        print('Given no. is not prime')
        return
    else:
        for i in range(3,n):
            if(n%i == 0):
                print('Given no. is not prime')
                i = i+1
                return
    print('Given number is prime')

isPrime(n)