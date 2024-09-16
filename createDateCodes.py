import datetime


def generate_dates(year_digits_num, startyear, startmonth, startday, endyear, endmonth, endday):

    # Generate all dates from 2022, 2023, 2024
    start_date = datetime.date(startyear, startmonth, startday)
    end_date = datetime.date(endyear, endmonth, endday)
    delta = datetime.timedelta(days=1)

    # List to store formatted dates
    dates_list = []
    # Loop through each day
    while start_date <= end_date:
        # Extract year, month, and day

        if year_digits_num != 2:
            year = f'{start_date.year}'
        else:
            year = f'{start_date.year % 100:02d}'

        month = f'{start_date.month:02d}'  # Formatting with leading zeros
        day = f'{start_date.day:02d}'  # Formatting with leading zeros

        # Different formats
        yyyymmdd = f"{year}{month}{day}"
        mmddyyyy = f"{month}{day}{year}"
        ddyyyymm = f"{day}{year}{month}"
        yyyyddmm = f"{year}{day}{month}"
        ddmmyyyy = f"{day}{month}{year}"
        mmyyyydd = f"{month}{year}{day}"

        # Add all formats to the list
        dates_list.extend((yyyymmdd, mmddyyyy, ddyyyymm, yyyyddmm, ddmmyyyy, mmyyyydd))

        # Increment to the next day
        start_date += delta
    return dates_list  # Return the list of formatted dates


def print_my_dates(year_digits_num, startyear, startmonth, startday, endyear, endmonth, endday):
    my_dates_list = (generate_dates(year_digits_num, startyear, startmonth, startday, endyear, endmonth, endday))
    for part in my_dates_list:
            print(part)

# for test uncomment it
#print_my_dates(2, 2022, 1, 1, 2024, 12, 31)

