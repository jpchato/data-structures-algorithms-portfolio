def fizz_buzz(number):
    if number % 15 == 0:
        print('fizzbuzz')
        return 
    elif number % 5 == 0:
        print('fizz')
        return
    elif number % 3 == 0:
        print('buzz')
        return
    else:
        print('Number not fizz, buzz, or fizzbuzz')


if __name__ == "__main__":
    fizz_buzz(1)
    fizz_buzz(3)
    fizz_buzz(5)
    fizz_buzz(15)