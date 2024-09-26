
import datetime
def display_current_datetime():
  current_date = datetime.datetime.now()
  formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current date and time: {formatted_date}")


def calculate_future_date(days):
 current_date = datetime.datetime.now()
 future_date = current_date + datetime.timedelta(days=days)
 formatted_future_date = future_date.strftime("%Y-%m-%d")
 print(f"Future date: {formatted_future_date}")
display_current_datetime()
number_of_days= int(input("Enter a number of days to add to the current date: "))
calculate_future_date(number_of_days)