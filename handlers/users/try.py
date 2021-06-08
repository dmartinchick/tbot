import datetime

text = [('обед',datetime.datetime(2021,6,19,14,0)), ('вывыв',datetime.datetime(2021,6,19,15,0)), ('xnj pf [',datetime.datetime(2021,6,20,18,0))]

def parse_line(text):
    name = text[0]
    dt = text[1].strftime('%d.%m %H:%M')
    answ = f"Название конкурса:\t{name} \nВремя проведения:\t{dt}"
    return answ    


def create_card(text):
    answ = ''
    for line in text:
        answ = answ + parse_line(line) + "\n\n"
    return answ

print(create_card(text))
# print(parse_line(text[0]))