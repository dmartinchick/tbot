import datetime

rq = [('Техника пешеходного туризма', datetime.datetime(2021, 6, 18, 13, 0), datetime.datetime(2021, 6, 18, 15, 30), 'r"data\\img\\hiking_technique.jpg"', 'cont_hiking_technique')]

for event in rq:
    event_name = event[0]
    time_start = event[1].strftime('%d.%m %H:%M')
    time_end = event[2].strftime('%d.%m %H:%M')
    address = event[3]
    contains = event[4]

print(time_start)