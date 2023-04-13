def fizz(self, number):
    number % 3 == 0
    return "fizz"

def buzz(self, number):
    number % 5 == 0
    return "buzz"

def fizz_buzz(self, number):
    number % 3 == 0 and number % 5 == 0
    return "fizzbuzz"

def fizz_buzz_number_to_string(self, number):
    number = str(number)
    return str(number)



#should have done it as one function!!! the below is the solution 
# def fizz_buzz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "fizzbuzz"
#     if number % 3 == 0:
#         return "fizz"
#     elif number % 5 == 0:
#         return "buzz"
#     return str(number)
