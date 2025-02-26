# Problem 1:
def replace_digit_with_word(number):
    digit_t = {
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
        '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
    }
    result = ""
    for digit in str(number):
        word = digit_t[digit]
        result = result + word
    return result

# Problem 2:
def count_specific_digit(number, digit_t):
    count = 0
    for digit in str(number):
        if digit == str(digit_t):
            count = count + 1
    return count

# Problem 3:
def sum_of_digits_consecutive_powers(number):
    digits = [int(digit) for digit in str(number)]
    total = 0
    position = 1
    for digit in digits:
        total = total + (digit ** position)
        position = position + 1
    return total

# Problem 4:
def has_all_unique_digits(number):
    seen_digits = set()
    for digit in str(number):
        if digit in seen_digits:
            return False
        seen_digits.add(digit)
    return True

# Problem 5:
def multiply_digits(number):
    product = 1
    for digit in str(number):
        product = product * int(digit)
    return product

# Problem 6:
def contains_digit(number, digit_t):
    for digit in str(number):
        if digit == str(digit_t):
            return True
    return False

# Problem 7:
def sum_even_position_digits(number):
    digits = [int(digit) for digit in str(number)]
    total = 0
    position = 1
    for digit in digits:
        if position % 2 == 0:
            total = total + digit
        position = position + 1
    return total

# Problem 8:
def swap_first_last_digit(number):
    digits = list(str(number))
    first_digit = digits[0]
    last_digit = digits[-1]
    digits[0] = last_digit
    digits[-1] = first_digit
    result = ""
    for digit in digits:
        result = result + digit
    return int(result)

# Problem 9:
def digit_difference(number):
    digits = [int(digit) for digit in str(number)]
    largest_digit = max(digits)
    small= min(digits)
    return largest_digit - small

# Problem 10:
def remove_digit(number, digit_to_remove):
    result = ""
    for digit in str(number):
        if digit != str(digit_to_remove):
            result = result + digit
    return int(result) if result else 0