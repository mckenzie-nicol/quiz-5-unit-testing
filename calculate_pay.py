"""
Mckenzie Nicol
Reza Hedieloo
"""


def calculate_pay(hours, wage):
    """
    Calculate employee pay.

    :param hours: a positive float
    :param wage: a positive float
    :precondition: hours is a positive float greater than or equal to 0
    :precondition: wage is a positive float greater than or equal to 0
    :postcondition: calculate the expected employee pay
    :return: weekly pay

    >>> calculate_pay(10, 10)
    100.0
    >>> calculate_pay(50.00, 10.00)
    600.0
    """
    pay = 0
    if hours > 40:
        overtime = (hours - 40) * (wage * 2)
        pay = (40 * wage) + overtime
    if 0 <= hours <= 40:
        pay = hours * wage
    return float(pay)





def main():
    """
    Execute the program.
    """


if __name__ == "__main__":
    main()
