from random import randint

def get_numbers_ticket(min,max,quantity):
    """
       Generate a list of unique random numbers within a given range.

       Parameters:
       min (int): The minimum value of the range. Must be greater than 0.
       max (int): The maximum value of the range. Must be less than or equal to 1000.
       quantity (int): The number of unique random numbers to generate.

       Returns:
       list: A sorted list of unique random numbers within the given range.
       """
    if min<=0 or max > 1000 or min > max:
        print("valid size")
    else:
        tickets = []
        while len(tickets) < quantity:
            number = randint(min,max)
            if number not in tickets:
                tickets.append(number)
    return sorted(tickets)

if __name__ == "__main__":
    try:
        minimal = int(input("Minimum:"))
        maximal = int(input("Maximum:"))
        quantity = int(input("Quantity:"))

        print("tickets", get_numbers_ticket(minimal, maximal, quantity) if get_number_ticket(minimal, maximal, quantity) else
              "No unique random numbers in this range.")
    except:
        print("Invalid input. Please enter numbers.")
