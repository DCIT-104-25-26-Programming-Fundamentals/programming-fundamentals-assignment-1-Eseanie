def main():
    num = int(input('Enter a number: '))


    def multiplication_table(number):
        for multiplier in range(1, 13):
            print(f"{number} X {multiplier} = {number * multiplier}")

    multiplication_table(num)

if __name__ == "__main__":
    main()