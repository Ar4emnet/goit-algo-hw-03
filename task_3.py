import re

def normalize_phone(phone_number):
    """
        Normalize a phone number to a standardized format for SMS delivery.

        The function takes a phone number as input and returns the normalized phone number.
        The normalization process involves removing any non-digit characters and adding a country code if necessary.

        Parameters:
        phone_number (str): The input phone number. It can be in various formats, such as with or without country code,
                            with or without parentheses, spaces, hyphens, or other special characters.
        """

    patern = r"[+]?\d"
    number = re.findall(patern, phone_number)
    number = ''.join(number)
    if len(number) <= 10:
        number = "+38"+number
    elif len(number) <= 11:
        number = number[:1]+"38"+number[1:]
    elif len(number) <= 12:
        number = "+"+number
    return number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+0 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
