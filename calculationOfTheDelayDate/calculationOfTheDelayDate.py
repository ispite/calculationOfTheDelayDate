from datetime import date, timedelta
import datetime
from workalendar.europe import Russia

def calc_delay_date(delay_in_days, dispatch_date_docs, type_of_days):
    loc_calend= Russia()
    if type_of_days == "work":
        payment_date_raw = loc_calend.add_working_days(dispatch_date_docs, delay_in_days)
        payment_date = loc_calend.find_following_working_day(payment_date_raw)
        return payment_date
    elif type_of_days == "calend":
        pass
        payment_date = dispatch_date_docs + timedelta(delay_in_days)
        return payment_date
    else:
        print("Invalid input type_of_days!")
        return None

#TEST BLOCK
print(calc_delay_date(15, datetime.datetime(2019, 2, 12), "work"))
print(calc_delay_date(15, datetime.date(2019, 2, 12), "work"))

print(calc_delay_date(15, datetime.date(2019, 2, 12), "calend"))




##########################
#USELESS CODEBLOCK FOR ME

#import os
#import sys
#from datetime import date

# Add vendor directory to module search path
#parent_dir = os.path.abspath(os.path.dirname(__file__))
#vendor_dir = os.path.join(parent_dir, 'vendor')

#sys.path.append(vendor_dir)

# Now you can import any library located in the "vendor" folder!
#from workalendar.europe import Russia





#loc_calend= Russia()
#now = datetime.datetime.now()
#print(now)
#new = now + timedelta(15)
#print(new)





#loc_calend= Russia()
#print(loc_calend.is_working_day(date(2019, 2, 16)))


#dispatch_date_docs = date(2019, 2, 16)
#delay_in_days = 15
#payment_date_raw = loc_calend.add_working_days(date(2019, 2, 16), delay_in_days)
#print(payment_date_raw)