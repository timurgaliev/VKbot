from flask import Flask, request, json
from flask_sslify import SSLify
from flask_sqlalchemy import SQLAlchemy
import datetime
import vk
import os
import pandas as pd

app = Flask(__name__)
sslify = SSLify(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


session = vk.Session()
api = vk.API(session, v=5.122)
token = 'your token here'
confirmation_token = 'your confiramtion toke here'

'''today = datetime.date.today().strftime("%d-%m-%Y")
tomorrow = (datetime.date.today()+datetime.timedelta(days=1)).strftime("%d-%m-%Y")
weekday_today = datetime.datetime.today().weekday()
weekday_tomorrow = (datetime.datetime.today() + datetime.timedelta(days=1)).weekday()
studying_week_number = str(datetime.datetime.today().isocalendar()[1]-35)
before_ny = str(abs(datetime.date(2020, 1, 1)-datetime.date.today())).split()[0]'''

timetable = {0: 'photo369955155_457247117_9ca595e83c38d3a9b8',
             1: 'photo369955155_457247118_edd5880976bcd3c944',
             2: 'photo369955155_457247119_99a9fc8ab6a429742a',
             3: 'photo369955155_457247120_2d451720a0464200c1',
             4: 'photo369955155_457247121_7e35e6fda4b8849b5a',
             5: 'photo369955155_457247122_df72e59aefc8bcd05e',
             6: 'photo369955155_457245926_dbf6f5a706b156389d'}

days = {'понедельник': 0, 'пн': 0,
        'вторник': 1, 'вт': 1,
        'среда': 2, 'ср': 2,
        'четверг': 3, 'чт': 3,
        'пятница': 4, 'пт': 4,
        'суббота': 5, 'сб': 5,
        'воскресенье': 6, 'вс': 6}


name_of_day = {1: 'Пн',
               2: 'Вт',
               3: 'Ср',
               4: 'Чт',
               5: 'Пт',
               6: 'Сб',
               7: 'Вс'}


scheldue_exel = '/bot/scheldue.xlsx'
timetable_exel = pd.read_excel(scheldue_exel, index_col='date')

icons = {0: '1&#8419;',    1: '2&#8419;',    2: '3&#8419;',
         3: '4&#8419;',    4: '5&#8419;',    5: '6&#8419;',
         6: '7&#8419;',    7: '8&#8419;',    8: '9&#8419;'}

fos = '/bot/table_fos.xlsx'
table_fos = pd.read_excel(fos, index_col='id')

id_fos_name_fos = {1: 'Антенные системы в системах мобильной связи',
    2: 'Безопасность жизнедеятельности',
    3: 'Введение в профессиональную деятельность',
    4: 'Введение в системотехническое проектирование',
    5: 'Вычислительная техника и информационные технологии',
    6: 'Геоинформационные технологии',
    7: 'Геоинформационные технологии при планировании систем мобильной связи',
    8: 'Защита ВКР, включая подготовку к процедуре защиты и процедуру защиты',
    9: 'Инженерная и компьютерная графика',
    10: 'Иностранный язык',
    11: 'Интегрированные системы мобильной связи',
    12: 'Интегрированные системы радиосвязи',
    13: 'Информатика',
    14: 'Информационные технологии систем мобильной связи',
    15: 'Испытания средств связи',
    16: 'История',
    17: 'Конструирование средств связи',
    18: 'Культурология',
    19: 'Математика',
    20: 'Метрология, стандартизация и сертификация',
    21: 'Обработка информации в системах мобильной связи',
    22: 'Общая теория связи',
    23: 'Общая физика',
    24: 'Основы мобильных радиотехнических систем',
    25: 'Основы передачи дискретных сообщений',
    26: 'Основы построения инфокоммуникационных систем и сетей',
    27: 'Основы радиотехнических систем',
    28: 'Основы систем мобильной связи',
    29: 'Основы теории сигналов и цепей в системах связи',
    30: 'Основы теории цепей',
    31: 'Правоведение',
    32: 'Прикладные информационные технологии',
    33: 'Производственная практика - научно-исследовательская работа',
    34: 'Производственная практика - преддипломная',
    35: 'Производственная практика – преддипломная',
    36: 'Производственная практика по получению профессиональных умений и опыта профессиональной деятельности',
    37: 'Психология',
    38: 'Радиоматериалы и радиокомпоненты',
    39: 'Радиопередающие устройства',
    40: 'Радиопередающие устройства (дополнительные главы)',
    41: 'Радиопередающие устройства в системах мобильной связи',
    42: 'Радиоприемные устройства',
    43: 'Радиоприемные устройства (дополнительные главы)',
    44: 'Радиоприемные устройства в системах мобильной связи',
    45: 'Распространение радиоволн и АФУ в системах мобильной связи',
    46: 'Русский язык и культура речи',
    47: 'Сети и системы мобильной связи',
    48: 'Сети и системы телекоммуникаций',
    49: 'Социология и политология',
    50: 'Специальные разделы физики',
    51: 'Стандарты цифрового телевидения',
    52: 'Статистические линейные оценки в мобильных системах связи',
    53: 'Статистические линейные оценки и управление',
    54: 'Схемотехника телекоммуникационных устройств',
    55: 'Татарский язык и культура речи',
    56: 'Теоретические основы систем мобильной связи',
    57: 'Теория колебаний',
    58: 'Теория коммутации в системах мобильной связи',
    59: 'Теория надежности',
    60: 'Теория решения исследовательских задач',
    61: 'Теория телетрафика',
    62: 'Техника микропроцессорных систем в мобильной связи',
    63: 'Техника микропроцессорных систем связи',
    64: 'Устройства СВЧ и антенны',
    65: 'Учебная практика по получению первичных профессиональных умений и навыков 1',
    66: 'Учебная практика по получению первичных профессиональных умений и навыков 2',
    67: 'Физическая культура и спорт',
    68: 'Физическая культура и спорт (элективная дисциплина)',
    69: 'Философия',
    70: 'Химия',
    71: 'Цифровая обработка сигналов',
    72: 'Цифровые стандарты мобильного телевидения',
    73: 'Экология',
    74: 'Экономика',
    75: 'Экономика, торговая политика и право ВТО, Таможенного союза и Зоны свободной торговли стран СНГ',
    76: 'Электромагнитная совместимость',
    77: 'Электромагнитные поля и волны',
    78: 'Электроника',
    79: 'Электропитание устройств и систем телекоммуникаций'}

def send_forward_message(user_id, random_id, token, peer_id, forward_messages, message="", attachment=""):
    api.messages.send(access_token=token, user_id=str(user_id), random_id=random_id, peer_id=peer_id, message=message, attachment=attachment, forward_messages=forward_messages)


def send_message(user_id, random_id, token,peer_id, message, attachment="", keyboard=""):
    api.messages.send(access_token=token, user_id=str(user_id), random_id=random_id,peer_id=peer_id, message=message, attachment=attachment, keyboard=keyboard)



def scheldue(time):
    res = ''
    t = timetable_exel.loc[time].shape[0]
    sort = timetable_exel.loc[time]
    for i in range(t):
        res += icons[i] + ' ' + str(sort['time'][i])[:5]+' '+str(sort['type'][i]) +'|'+str(sort['room'][i]) +\
            '|'+ str(sort['building'][i]) + ' ' + str(sort['subject'][i]) +\
            ' ' + '\t' +  str(sort['surname'][i]) +'\n'
    return res


def get_fos():
    res = "ID и название предмета \n"
    for id, name in id_fos_name_fos.items():
        res += str(id) + " " + name + "\n"
    return res


def get_fos_id(id):
    res = str(id) + " " + id_fos_name_fos[id] + "\n"
    t = table_fos.loc[id].shape[0]
    sort = table_fos.loc[id]
    for i in range(t):
        res += str(sort['doc'][i:i+1].item()) + "\n" + str(sort['link'][i:i+1].item()) + "\n"
    return res


def timetable_for_current_week():
    text = ''
    for i in range(7 - datetime.datetime.today().isocalendar()[2]):
        d = (datetime.datetime.today()+datetime.timedelta(days=i)).isocalendar()[2]
        day = datetime.date.today()+datetime.timedelta(days=i)
        t = scheldue(str(day))
        if len(t) == 0:
            t = 'Занятий нет'
        text += '\n' + str(name_of_day[d]) + ': ' + str(day.strftime("%d-%m-%Y")) + '\n' + t + '\n'
    return text


def oddness_evenness_week():
    if datetime.datetime.today().isocalendar()[1] % 2 == 0:
        week = 'нечетная'
    else:
        week = 'четная'
    return week


def oddness_evenness_week_tomorrow():
    if (datetime.datetime.today()+datetime.timedelta(days=1)).isocalendar()[1] % 2 == 0:
        week = 'нечетная'
    else:
        week = 'четная'
    return week


def oddness_evenness_week_next_tomorrow():
    if (datetime.datetime.today()+datetime.timedelta(days=2)).isocalendar()[1] % 2 == 0:
        week = 'нечетная'
    else:
        week = 'четная'
    return week


class User(db.Model):
    __tablename__ = 'list'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, index=True)
    forward_number = db.Column(db.Integer, default=0)
    '''subject_name = db.Column(db.Text, nullable=True)
    deadline = db.Column(db.Text, nullable=True)
    photo = db.Column(db.Text, nullable=True)
    comments = db.Column(db.Text, nullable=True)
    order = db.Column(db.Integer, nullable=True)'''

    def __repr__(self):
        return 'User %r' % self.name


db.create_all()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = json.loads(request.data)
        if 'type' not in data.keys():
            return 'not vk'
        if data['type'] == 'confirmation':
            return confirmation_token
        message = data['object']['message'].get('text', '').lower()
        if len(message) is 0:
            message += 'text'
        message_split = message.split()
        random_id = data['object']['message']['id']
        user_id = data['object']['message']['from_id']
        forward_messages = data['object']['message']['id']
        peer_id = data['object']['message']['peer_id']
        names = User.query.filter_by(name=message)
        if 'привет' in message:
            send_message(user_id, random_id, token, peer_id, 'Привет')
            return 'ok'
        if '*' in message_split[0]:
            if user_id in {369955155, 1}:
                add = User(name=message_split[1], forward_number=forward_messages)
                db.session.add(add)
                send_message(user_id,random_id, token, peer_id, 'Добавлено')
                db.session.commit()
            else:
                send_message(user_id,random_id, token,peer_id, 'You are NOT allowed to add messages!')
            return 'ok'
        if 'del' in message_split[0]:
            if user_id in {369955155, 1} and message_split[2] == 'id':
                for i in range(User.query.filter_by(name=message_split[1]).count()):
                    send_forward_message(user_id,random_id, token,peer_id, User.query.filter_by(name=message_split[1])[i].forward_number)
                    send_message(user_id,random_id, token,peer_id, str(User.query.filter_by(name=message_split[1])[i].forward_number))
            elif user_id in {369955155, 1} and message_split[2] is not 'id':
                delete = User.query.filter_by(forward_number=int(message_split[2])).first()
                db.session.delete(delete)
                db.session.commit()
                send_message(user_id,random_id, token,peer_id, 'deleted')
            else:
                send_message(user_id,random_id, token,peer_id, 'You are NOT allowed to delete messages!')
            return 'ok'
        if User.query.filter_by(name=message).first() is not None:
            update_string = []
            for i in range(User.query.filter_by(name=message).count()):
                update_string.append(names[i].forward_number)
            send_forward_message(user_id,random_id, token,peer_id, ','.join(str(i) for i in update_string))
            return 'ok'
        if 'послезавтра' in message:
            send_message(user_id,random_id, token,peer_id, 'Расписание на послезавтра ' +
                         str((datetime.date.today() + datetime.timedelta(days=2)).strftime("%d-%m-%Y"))
                         + ' (' + oddness_evenness_week_next_tomorrow() + ')' + ':\n' +
                         scheldue(str(datetime.date.today() + datetime.timedelta(days=2))))
            return 'ok'
        if 'сегодня' in message:
            send_message(user_id,random_id, token,peer_id, 'Расписание на сегодня ' + str(datetime.date.today().strftime("%d-%m-%Y"))
                         + ' (' + oddness_evenness_week() + ')' + ':\n' + scheldue(str(datetime.date.today())))
                         #str(timetable[datetime.datetime.today().weekday()]))
            return 'ok'
        if 'завтра' in message:
            send_message(user_id,random_id, token,peer_id, 'Расписание на завтра ' +
                         str((datetime.date.today()+datetime.timedelta(days=1)).strftime("%d-%m-%Y"))
                         + ' (' + oddness_evenness_week_tomorrow() + ')' + ':\n'+
                         scheldue(str(datetime.date.today()+datetime.timedelta(days=1))))
                         #str(timetable[(datetime.datetime.today() + datetime.timedelta(days=1)).weekday()]))
            return 'ok'
        if message in days:
            send_message(user_id,random_id, token,peer_id, 'Расписание на: ' + str(message), str(timetable[days[message]]))
            return 'ok'
        if 'неделя' in message:
            send_message(user_id,random_id, token,peer_id, '&#128260;' + oddness_evenness_week() + '\n' +
                         '&#9203;Учебная неделя: ' + str(datetime.datetime.today().isocalendar()[1]-4)
                         + '\n' + str(timetable_for_current_week())
                         )
            return 'ok'
        if 'помощь' in message:
            send_message(user_id,random_id, token,peer_id, '&#127891; Расписание: \n-расписание или сегодня\n-завтра\n-день недели\n'
                                         '-неделя\n' + '&#128229; - Информация\n' + '&#128115; - Фамилия преподавателя')

            return 'ok'
        if 'фосы' in message:
            send_message(user_id, -1*random_id, token, peer_id, "Для того, чтобы получить ФОС по какому-либо предмету, необходимо ввести сообщение 'фос ID', где ID - номер из списка")
            send_message(user_id, random_id, token, peer_id, get_fos())
            return 'ok'
        if 'фос' in message_split[0]:
            if (message_split[0]!= message and message_split[1].isdigit() and 1 <= int(message_split[1]) <= 79 ):
                send_message(user_id, random_id, token, peer_id, get_fos_id(int(message_split[1])))
            else:
                send_message(user_id, random_id, token, peer_id, "Ошибка ввода ID")
            return 'ok'
        if 'расписание' in message:
            send_message(user_id,random_id, token,peer_id, "Выберите день", "", open(os.path.join(basedir, 'timetable.json'), 'r').read())
            return 'ok'
        if 'назад' in message:
            send_message(user_id,random_id, token,peer_id, "Выберите опцию", "",
                         open(os.path.join(basedir, 'main_keyboard.json'), 'r').read())
            return 'ok'
        if 'день недели' in message:
            send_message(user_id,random_id, token,peer_id, "Выберите день недели", "",
                         open(os.path.join(basedir, 'weekday.json'), 'r').read())
            return 'ok'
        if 'преподаватели' in message:
            send_message(user_id,random_id, token,peer_id, "Веберите преподавателя", "",
                         open(os.path.join(basedir, 'teachers_keyboard.json'), 'r').read())
            return 'ok'
        if 'начать' in message:
            send_message(user_id,random_id, token,peer_id, "Добро пожаловать. Я бот группы 5305. \n "
                                         "Мои команды можно узнать через команду: помощь \n", "",
                         open(os.path.join(basedir, 'main_keyboard.json'), "r").read())
            return 'ok'
        if 'время' in message:
            send_message(user_id,random_id, token,peer_id, 'Время на сервере: ' +
                                          str(datetime.datetime.today().strftime("%d-%m-%Y %H:%M:%S")))
            return 'ok'
        if 'спасибо' in message:
            send_message(user_id,random_id, token,peer_id, 'Не стоит благодарности!')
            return 'ok'
        else:
            send_message(user_id,random_id, token,peer_id, 'Ошибка! Ничего не найдено \n Чтобы увидеть мои команды введите: помощь', "")

        db.session.commit()
    return 'ok'


if __name__ == '__main__':
    app.run()
