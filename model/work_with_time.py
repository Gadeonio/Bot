from datetime import datetime, time, timedelta

format = "%H:%M:%S"


def check_format_time_with_datetime(text):
    global format
    try:
        print(datetime.strptime(text, format))
        res = bool(datetime.strptime(text, format))

    except ValueError:
        print("Incorrect data format, should be HH:MM:SS")
        res = False
    return res


def addition_times(str_time1: str, str_time2: str):
    h1, m1, s1 = tuple_float(str_time1)
    h2, m2, s2 = tuple_float(str_time2)
    str_time = str(timedelta(hours=h1, minutes=m1, seconds=s1) + timedelta(hours=h2, minutes=m2, seconds=s2))
    str_time = get_time_without_days(str_time)
    h_sum, m_sum, s_sum = map(lambda x: int(x), time_as_tuple(str_time))
    return time(h_sum, m_sum, s_sum).isoformat(timespec='seconds')


def subtraction_times(str_time1: str, str_time2: str):
    h1, m1, s1 = tuple_float(str_time1)
    h2, m2, s2 = tuple_float(str_time2)
    str_time = str(timedelta(hours=h1, minutes=m1, seconds=s1) - timedelta(hours=h2, minutes=m2, seconds=s2))
    str_time = get_time_without_days(str_time)
    h_sum, m_sum, s_sum = map(lambda x: int(x), time_as_tuple(str_time))
    return time(h_sum, m_sum, s_sum)


def get_time_without_days(str_time: str):
    if check_have_day(str_time):
        str_time = str_time[str_time.index('day') + 5:]
    return str_time


def is_day_get_subtraction_times(str_time1: str, str_time2: str):
    h1, m1, s1 = tuple_float(str_time1)
    h2, m2, s2 = tuple_float(str_time2)
    str_time = str(timedelta(hours=h1, minutes=m1, seconds=s1) - timedelta(hours=h2, minutes=m2, seconds=s2))
    if check_have_day(str_time):
        return True
    return False


def is_day_get_addition_times(str_time1: str, str_time2: str):
    h1, m1, s1 = tuple_float(str_time1)
    h2, m2, s2 = tuple_float(str_time2)
    str_time = str(timedelta(hours=h1, minutes=m1, seconds=s1) + timedelta(hours=h2, minutes=m2, seconds=s2))
    if check_have_day(str_time):
        return True
    return False


def check_have_day(str_time: str):
    if str_time.find("day") > -1:
        return True
    return False


def time_as_tuple(str_time: str):
    h, m, s = tuple(str_time.split(':'))
    return h, m, s


def tuple_float(str_time):
    return map(lambda x: float(x), time_as_tuple(str_time))
