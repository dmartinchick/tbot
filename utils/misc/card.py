from datetime import datetime


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
