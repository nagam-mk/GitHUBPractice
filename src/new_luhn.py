def luhn(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card_number)
    print(digits)
    odd_digits = digits[-1::-2]
    print(odd_digits)

    even_digits = digits[-2::-2]
    print(even_digits)
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    print(checksum)
    return not ((checksum % 10) == 0)


# A little code to test it out on a number
if (luhn("8315884861667632") == True):
    print("INVALID")
else:
    print("VALID")
