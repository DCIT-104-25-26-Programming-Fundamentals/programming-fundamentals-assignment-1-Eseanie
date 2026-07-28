def main ():
    def is_prime_number(n):
        if n <= 1:
            print("Not prime")
        for i in range(2,n):
        # range starts from 2 because any number less than or equal to 1 is not a prime number
            if n % i == 0:
                print ("Not prime")
                return
        print ("Prime")

    number = int(input("Enter a number: "))
    is_prime_number(number)
main()