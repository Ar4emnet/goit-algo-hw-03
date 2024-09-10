from datetime import datetime


def get_days_from_today(date=None):
    try:
        """
        Calculate the number of days between a given date and today's date.

        Parameters:
        date (str): A string representing the date in the format 'YYYY-MM-DD'. If not provided, the function will use today's date.

        Returns:
        int: The number of days between the given date and today's date. If the given date is in the future, the result will be positive. If the given date is in the past, the result will be negative.
        """
        today = datetime.today().date()
        date = datetime.strptime(date, '%Y-%m-%d').date()
        return (date - today).days
    except:
        print('incorrect input format')


if __name__ == '__main__':
    print('this date will be in', get_days_from_today(input('write date in format Year-month-day ')), "days")