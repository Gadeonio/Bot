import json

from model.work_with_time import *
import model.json_manipulation


def check_employment_with_int(time1: tuple, time2: tuple):
    start1, end1 = time1
    start2, end2 = time2

    if start1 - end2 >= 0 or start2 - end1 >= 0:
        return False
    return True


def check_employment_with_str(time1: tuple, time2: tuple):
    start1, end1 = time1
    start2, end2 = time2
    if not is_day_get_subtraction_times(start1, end2) or not is_day_get_subtraction_times(start2, end1):
        return False
    return True


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, RoomTimeList):
            return obj.__dict__
        elif isinstance(obj, Room):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


class RoomTimeList:
    def __init__(self, room, time_list=None):
        if time_list is None:
            time_list = []
        self.room = room
        self.time_list = time_list


class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == self.name


class BaseReservation:
    def __init__(self, rooms=None):
        if rooms is None:
            print("Adding list room")
            self.rooms_time_list = []
        else:
            '''rooms.sort()
            rooms.reverse()'''
            self.rooms_time_list = list(map(lambda x: RoomTimeList(x), rooms))

    def __str__(self):
        res_str = "BaseReservation\n"
        for i in self.rooms_time_list:
            res_str += f"Room {i.room}: {i.time_list}\n"
        return res_str

    def add_reservation(self, start_time: str, end_time="", duration="", room=None):
        if end_time == "" and duration == "":
            print("Введите время окончания или длительность")
            return
        if room is None:
            if end_time == "":
                self.add_reservation_duration(start_time, duration)
            else:
                self.add_reservation_times(start_time, end_time)
        else:
            if end_time == "":
                self.add_reservation_duration_with_room(start_time, duration, room)
            else:
                self.add_reservation_times_with_room(start_time, end_time, room)

    def get_spare_room_times(self, start_time, end_time):
        for room_time_list in self.rooms_time_list:
            if not self.is_room_employment(room_time_list.time_list, start_time, end_time):
                return room_time_list
        return None

    def is_room_employment(self, times, start_time, end_time):  # rooms_time_list - список времен, на эту комнату
        desired_time = (start_time, end_time)
        for busy_time in times:
            if check_employment_with_str(busy_time, desired_time):
                return True
        return False

    def add_reservation_times(self, start_time, end_time):
        # Рассматриваем комнаты по capacity, если комната занята на это время, то нужно перейти к следующему объекту
        print("Запись по окончанию времени")
        room_time_list = self.get_spare_room_times(start_time, end_time)
        if room_time_list is not None:
            room_time_list.time_list.append((start_time, end_time))
            print(f"Забронирована комната {room_time_list.room} с {start_time}, {end_time}")
        else:
            print("Отсутствует возможность брони, все комнаты заняты")

    def add_reservation_duration(self, start_time: str, duration: str):
        print("Запись по длительности")
        end_time = addition_times(start_time, duration)
        self.add_reservation_times(start_time, end_time)

    def add_reservation_duration_with_room(self, start_time, duration, room):
        print("Данная функций пока не проработана")
        pass

    def add_reservation_times_with_room(self, start_time, end_time, room):
        print("Данная функций пока не проработана")
        pass

    def save_in_json_file(self):
        name = "rooms_time_list"
        model.json_manipulation.create_json_file(f"{name}.json", self.rooms_time_list, cls=JsonEncoder)

    def read_in_json_file(self):
        name = "rooms_time_list"
        data =  model.json_manipulation.read_json_file(f"{name}.json")
        self.rooms_time_list = []
        for i in data:
            self.rooms_time_list.append(RoomTimeList(Room(i['room']['name'], i['room']['capacity']), i['time_list']))


'''if __name__ == "__main__":
    zoo = Room('Zoo', 100)
    small_bed = Room('Small bed', 1)
    big_bed = Room('Big bed', 2)

    rooms = [zoo, small_bed, big_bed]
    reservation = BaseReservation()
    
    #Создали список брони, у каждой комнаты список из кортежей (время начала, длительность), и еще нужно будет сделать проверку
    #Возможно, но не обязательно создать функцию, принимающая время начала, длительность и если указывается, то и комнату
    #Попробовать сделать функцию, которая может бронировать по времени начала и окончания

    print(reservation)
    reservation.add_reservation("00:00:00", end_time="", duration="4:00:00")
    reservation.add_reservation("00:00:00", end_time="23:59:59")
    reservation.add_reservation("04:00:00", end_time="23:59:59")
    reservation.add_reservation("00:00:00", end_time="23:59:59")
    reservation.add_reservation("00:00:00", end_time="23:59:59")

    print(reservation)
    reservation.read_in_json_file()
    print("\n")
    print(reservation)'''
