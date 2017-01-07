#Anton Gefvert antge210, Aleksi Evansson aleev379
#7. Abstraktion
#Uppgift 7a




def start_time(ts):
    "span -> hour x minute"
    ensure(ts, is_time_span)
    return ts[1][0]

def end_time(ts):
    "span -> hour x minute"
    ensure(ts, is_time_span)
    return ts[1][1]

def overlap(ts1, ts2):
	"span x span -> span"
	ensure(ts1, is_time_span)
	ensure(ts2, is_time_span)
	min1 = max(ts1[1][0][1][0][1]*60+ts1[1][0][1][1][1], ts2[1][0][1][0][1]*60+ts2[1][0][1][1][1])
	min2 = min(ts1[1][1][1][0][1]*60+ts1[1][1][1][1][1], ts2[1][1][1][0][1]*60+ts2[1][1][1][1][1])
	return ('span', (('time', (('hour', min1//60), ('minute', min1%60))), ('time', (('hour', min2//60), ('minute', min2%60)))))

def new_duration(hour, minute):
    "hour x minute -> duration"
    ensure(hour, is_hour)
    ensure(minute, is_minute)
    return ('duration', (('hour', hour[1] + minute[1] // 60), ('minute', minute[1] % 60)))

def length_of_span(ts):
    "span -> duration"
    ensure(ts, is_time_span)
    mins = ts[1][1][1][1][1] + ts[1][1][1][0][1]*60 - ts[1][0][1][1][1] - ts[1][0][1][0][1]*60
    return ('duration', (('hour', mins//60), ('minute', mins%60)))