#Anton Gefvert antge210, Aleksi Evansson aleev379
#7. Abstraktion
#Uppgift 7d

def show_free(cal_name, d, m, t1, t2):
    "string x integer x string x string x string ->"
    day = new_day(d)
    mon = new_month(m)
    cal_day = calendar_day(day, calendar_month(mon, fetch_calendar(cal_name)))
    t1 = convert_time(t1)
    t2 = convert_time(t2)

    new_date(day, mon) 			# Ensure that the date is proper

    show_time_spans(free_spans(cal_day, t1, t2))


def free_spans(cal_day, t1, t2):
    "calendar_day x time x time -> time_spans"
    spans = new_time_spans()
    for app in strip_tag(cal_day):
        spans = insert_time_span(get_span(app), spans) 
    returnSpans = new_time_spans()
    tempStart = t1
    tempEnd = t2
    for span in strip_tag(spans):
        if precedes(start_time(span),t1):
            if precedes(end_time(span),t1):
                pass
            elif precedes(t2, end_time(span)):
                return returnSpans
            else:
                tempStart = end_time(span)
        elif is_same_time(tempStart, start_time(span)):
            if precedes(end_time(span),t2):
                tempStart = end_time(span)
            else:
                return returnSpans
        elif precedes(tempStart, start_time(span)) and precedes(start_time(span),t2):
            tempEnd = start_time(span)
            returnSpans = insert_time_span(new_time_span(tempStart, tempEnd),returnSpans)
            tempStart = end_time(span)

    if precedes(tempStart, t2):
        returnSpans = insert_time_span(new_time_span(tempStart, t2), returnSpans)
    return returnSpans


# -------- YOUR TEST CASES GO HERE -----------------------   
# For each case, add a brief description of what you want to test.
new_test_case(
        2,
        "08:00",
        "21:00",
        ["07:00-13:00", "13:00-21:00"], 
        [])
new_test_case(
        3,
        "08:00",
        "21:00",
        ["09:00-13:00", "13:00-22:00"], 
        ["08:00-09:00"])
new_test_case(
        4,
        "08:00",
        "21:00",
        ["07:00-23:00"],
        [])
new_test_case(
        5,
        "08:00",
        "21:00",
        ["07:00-08:00","21:00-22:00"],
        ["08:00-21:00"])
new_test_case(
        6,
        "08:00",
        "21:00",
        ["08:00-09:00","22:00-23:00"],
        ["09:00-21:00"])

"""
Motivering för testfall:
Vi har testfall där
*Bokningen börjar innan och slutar innan testintervall
*Börjar innnan och slutar på starttid
*Börjar innan och slutar inom testintervall
*Börjar på starttid och slutar inom testintervall
*Börjar och slutar inom testintervallet
*Börjar inom testintervall och slutar på sluttid
*Börjar inom testintervall och slutar efter
*Börjar på sluttid och slutar efter
*Börjar efter och slutar efter
*Tid som slutar på början av annan tid

Alltså testar vi alla fall som kan förekomma
"""
