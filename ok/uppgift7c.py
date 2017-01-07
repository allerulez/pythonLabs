#Anton Gefvert antge210, Aleksi Evansson aleev379
#7. Abstraktion
#Uppgift 7c

"""
vikho 12/7: Ok
Ser bra ut överlag, hade dock gärna sätt en implementation med not_is_booked_from
då det brukar leda till en renare lösning av remove istället för att jämföra
taggar osv. 

"""

# In calendar.py
def remove(cal_name, d, m, t1):
    "string x integer x string x string ->"
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

# In booking.py
def remove_appointment(cal_year, day, mon, time):
    "calendar_year x day x month x time -> calendar_year"
    cal_day = calendar_day(day, calendar_month(mon, cal_year))
    return insert_calendar_month(
                mon,
                insert_calendar_day(
                    day,
                    erase_appointment(cal_day, time),
                    calendar_month(mon, cal_year)),
                cal_year)

    
# In calendar_ADT.py
def erase_appointment(cal_day, time):
    "calendar_day x time -> calendar_day"
    new_cal_day = new_calendar_day()
    removed = False
    for app in strip_tag(cal_day):
        if not is_same_time(time, start_time(get_span(app))):
            new_cal_day = insert_appointment(app, new_cal_day)
    return new_cal_day


# In calendar.py
def help():
    print('The Calendar. \n\n')
    print('-'*50)
    print('A quick reminder of your options:')
    print('  create(name)')
    print('  book(name, day, month, time, subject)')
    print('  remove(name, day, month, time') #Added
    print( ' show(name, day, month)')
    print( ' save(filename)')
    print( ' load(filename)')


if __name__ == "__main__":
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

"""
+--------+         +--------------------+         +-------------------+
| remove |>--->--->| remove_appointment |>--->--->| erase_appointment |
+--------+         +--------------------+         +-------------------+
"""
