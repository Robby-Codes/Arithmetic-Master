import pickle
import re
from random import randint


def error_message():
    data = pickle.load(open('storage.dat', 'rb'))
    message = ''
    if data['min_error'] is True:
        message += "There is an Error in your custom 'Min' input\n"
    if data['max_error'] is True:
        message += "There is an Error in your custom 'Max' input\n"
    if data['deci_error'] is True:
        message += "There is an Error in your custom 'Deci' input"
    return message


def custom_min(min_):
    data = pickle.load(open('storage.dat', 'rb'))
    result = False
    if (re.match(r'^[0-9]+$', min_) and
            not re.match(r'^0+[1-9]+$', min_) and
            int(min_) <= data['max_data']):
        result = True
    if result:
        data['min_error'] = False
        pickle.dump(data, open('storage.dat', 'wb'))
        return True
    else:
        data['min_error'] = True
        pickle.dump(data, open('storage.dat', 'wb'))
        return False


def custom_max(max_):
    data = pickle.load(open('storage.dat', 'rb'))
    result = False
    if (re.match(r'^[0-9]+$', max_) and
            not re.match(r'^0+[1-9]+$', max_) and
            int(max_) >= data['min_data']):
        result = True
    if result:
        data['max_error'] = False
        pickle.dump(data, open('storage.dat', 'wb'))
        return True
    else:
        data['max_error'] = True
        pickle.dump(data, open('storage.dat', 'wb'))
        return False


def custom_deci(deci):
    data = pickle.load(open('storage.dat', 'rb'))
    result = False
    if deci is not None:
        if (re.match(r'^[0-9]+$', deci) and
                not re.match(r'^0+[1-9]+$', deci) and
                int(deci) <= 14):
            result = True
    if result:
        data['deci_error'] = False
        pickle.dump(data, open('storage.dat', 'wb'))
        return True
    else:
        data['deci_error'] = True
        pickle.dump(data, open('storage.dat', 'wb'))
        return False


def create_deci(deci_places):
    for digits in range(deci_places):
        if digits == 0:
            num = '.'
        num += str(randint(0, 9))
    return num


def create_neg(num):
    chance = randint(1, 2)
    return -num if chance == 1 else num


def begin_adding(data_set):
    if (data_set['min_error'] is True or
            data_set['max_error'] is True or
            data_set['deci_error'] is True):
        return error_message()
    else:
        num1 = randint(data_set['min_data'], data_set['max_data'])
        num2 = randint(data_set['min_data'], data_set['max_data'])
        num3, num4 = '', ''
    if data_set['deci_data'] != 0:
        num3 = create_deci(data_set['deci_data'])
        num4 = create_deci(data_set['deci_data'])
    if data_set['neg_data']:
        num1 = create_neg(num1)
        num2 = create_neg(num2)
    return '   ' + str(num1) + num3 + '\n+ ' + str(num2) + num4


def prepare_data(key=False, min_=None, max_=None, deci=None, neg=None):
    if key is True:
        data = dict(
            min_data=0, max_data=100, deci_data=0, neg_data=False,
            min_error=False, max_error=False, deci_error=False)
        pickle.dump(data, open('storage.dat', 'wb'))
    else:
        data = pickle.load(open('storage.dat', 'rb'))
        if min_ is not None:
            data['min_data'] = min_
        if max_ is not None:
            data['max_data'] = max_
        if deci is not None:
            data['deci_data'] = deci
        if neg is not None:
            data['neg_data'] = neg
        pickle.dump(data, open('storage.dat', 'wb'))
    return begin_adding(data)


def answer(user_ans, problem):
    if (re.match(r'^-?[0-9]+\.?[0-9]*$', user_ans) and
            not re.match(r'^There', problem)):
        if eval(user_ans) == eval(problem.replace('\n', '')):
            return True
    else:
        return False
