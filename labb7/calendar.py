
# =========================================================================
#  The Calendar - Functional and imperative programming in Python
#
#  Module: calendar.py
#  Updated: 2004-11-10 by Peter Dalenius
#   Translated to Python in 2012 by Peter L-G
#   Translated to English in 2013 by Anders M.L.
#  Dependencies:
#   calendar_ADT.py
#   booking.py
#   output.py
# =========================================================================

# This module ties the calendar together. It contains the functions 
# that users interact with, and the global dictionary where all 
# calendars are stored.

# Functions in this file never delve deeper into the representation of the 
# calendar objects, or the internal logic of actually booking an appointment,
# are available in separate modules. These are imported automatically upon the
# import of the calendar module.

# The files have the following dependencies:

#
#               calendar.py
#                   |
#           +_______+________+
#           |                |
#      booking.py      output.py
#           |                |
#           +_______+________+ 
#                   |
#              calendar_ADT.py


from calendar_ADT import *
from booking import *
from output import *


import pickle;

# =========================================================================
#  1. Storing and fetching calendars
# =========================================================================
calendars = dict();

def fetch_calendar(cal_name):
    if calendar_exists(cal_name):
        return calendars[cal_name]
    else:
        raise Exception("There is no calendar_year by the name {0}.".format(cal_name))

def insert_calendar(cal_name, cal_year):
    calendars[cal_name] = cal_year
    return calendars

def calendar_exists(cal_name):
    return cal_name in calendars

def new_calendar(cal_name):
    calendars[cal_name] = new_calendar_year()
    return calendars

# Saves all calendars to file. The data is wrapped in [*CALFILE2000*, ...] which is
# used as a tag for identifying calendar files.
def save_calendars(filename):
    "String ->"
    output = open(filename, 'wb')
    pickle.dump(['*CALFILE2000*', calendars], output)
    output.close()

# Loads calendar from a file. If the file does not exist, or is malformed,
# the calendars remain as they are.

# The file to be loaded is assumed to be non-hostile (cf the warning in the Pickle 
# module documentation http://docs.python.org/3/library/pickle.html ).

def load_calendars(filename):
    "String -> Bool"
    try:
        pkl_file = open(filename, 'rb')
        file_content = pickle.load(pkl_file)
        pkl_file.close()
        if isinstance(file_content, list) and\
         len(file_content) == 2 and\
         file_content[0] == '*CALFILE2000*':
            global calendars
            calendars = file_content[1]
            return True
        else:
            return False
    except IOError:
        return False

# =========================================================================
#  2. User interface
# =========================================================================

def create(cal_name):
    "String ->"
    if calendar_exists(cal_name):
        print("A calendar by the name {0} already exists.".format(cal_name))
    else:
        new_calendar(cal_name)
        print("A new calendar by the name {0} has been created.".format(cal_name))

def show_calendars():
    "->"
    if calendars:
        print("The following calendars exist:")
        for cal_name in calendars:
            print(cal_name)
    else:
        print("No calendars have been created.")

def book(cal_name, d, m, t1, t2, subject_text):
    "String x Integer x String x String x String x String ->"
    day = new_day(d)
    mon = new_month(m)
    start = convert_time(t1)
    end = convert_time(t2)
    subject = new_subject(subject_text)
    cal_day = calendar_day(day, calendar_month(mon, fetch_calendar(cal_name)))
    
    new_date(day, mon) # Ensure that the date is proper
    
    if precedes(end, start):
        print("Invalid appointment time (wrong order of start and finish).")
    elif is_booked(cal_day, new_time_span(start, end)):
        print("The proposed time is already taken.")
    else:
        insert_calendar(cal_name, book_appointment(fetch_calendar(cal_name),
                                          day, mon, start, end, subject))
        print("The appointment has been booked.")

def remove(cal_name, d, m, t1):
    day = new_day(d)
    mon = new_month(m)
    start = convert_time(t1)
    cal_year = fetch_calendar(cal_name)
    
    new_date(day, mon) # Ensure that the date is proper
    remove_year = remove_appointment(cal_year, day, mon, start)
    if strip_tag(remove_year) != strip_tag(cal_year): 
        insert_calendar(cal_name, remove_year)
        print("Appointment removed.")
    else:
        print("No appointment at this time and date")

def show(cal_name, d, m):
    "String x Integer x String ->"
    day = new_day(d)
    mon = new_month(m)
    cal_day = calendar_day(day, calendar_month(mon, fetch_calendar(cal_name)))
    
    new_date(day, mon) 			# Ensure that the date is proper
    
    if is_empty_calendar_day(cal_day):
        print("No appointments this day.\n")
    else:
        show_day_heading(day, mon)
        show_calendar_day(cal_day)

def show_free(cal_name, d, m, t1, t2):
    "string x integer x string x string x string ->"
    day = new_day(d)
    mon = new_month(m)
    cal_day = calendar_day(day, calendar_month(mon, fetch_calendar(cal_name)))
    t1 = convert_time(t1)
    t2 = convert_time(t2)

    new_date(day, mon) 			# Ensure that the date is proper

    show_time_spans(free_spans(cal_day, t1, t2))
    

def save(filename):
    "String ->"
    save_calendars(filename)
    print("The calendars have been saved to {0}.".format(filename))

def load(filename):
    "String ->"
    if load_calendars(filename):
        print("New calendars have been loaded.")
    else:
        print("The file does not exist, or it is devoid of saved calendars.")

        
def help():
    print('The Calendar. \n\n')
    print('-'*50)
    print('A quick reminder of your options:')
    print('  create(name)')
    print('  book(name, day, month, time, subject)')
    print('  remove(name, day, month, time')
    print( ' show(name, day, month)')
    print( ' save(filename)')
    print( ' load(filename)')

create("greger")
book("greger", 24, "dec", "15:00", "16:00", "Charlie anka")
book("greger", 24, "dec", "17:00", "18:00", "Äta räkor")
show("greger", 24, "dec")
remove("greger", 24, "dec", "17:00")
book("greger", 24, "dec", "18:00", "19:00", "Äta rökta räkor med aioli")
show("greger", 24, "dec")
remove("greger", 24, "dec", "16:00")
remove("greger", 24, "dec", "20:00")
show("greger", 24, "dec")

create("Peter")
book("Peter", 24, "dec", "07:00", "07:30","test")
book("Peter", 24, "dec", "08:30", "09:00","test1")
book("Peter", 24, "dec", "10:00", "11:22","test2")
book("Peter", 24, "dec", "12:13", "12:14","test3")
book("Peter", 24, "dec", "17:00", "20:59","test4j")
book("Peter", 24, "dec", "21:00", "21:30","test5")
book("Peter", 24, "dec", "22:00", "23:00","testk")
