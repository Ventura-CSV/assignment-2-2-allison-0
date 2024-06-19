def main():

    # Comlete your code here
    # Use the same variables: celsius fahrenheit 
    celsius = float(input('Enter the temperature in celsius'))
    fahrenheit = float(((9/5) * celsius)+32)
    # Do not delete the return statement
    print(fahrenheit)

    return celsius, fahrenheit


if __name__ == '__main__':
    main()
