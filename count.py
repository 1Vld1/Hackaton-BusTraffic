import GetData
import datetime

#
#
BUS_SPEED = 40  # скорость автобуса в километрах в час
STOP_TIME = 2  # время остановки в минутах
REST_TIME = 15  # время между рейсами в депо в минутах
PAS_CAP_MIN = 85
PAS_CAP_MAX = 105
#
#
passenger_thread = []  # пассажиропоток, позже добавить сюда значения ПП по
rout_dict = {}  # информация о маршрутах
routs_info = {}
def config_sys():
    passenger_thread.extend(GetData.Get_passengers_thread_in_day())
    routs_info.update(GetData.Get_routs_info())
    rout_dict.update(routs_info['Номер маршрута'])


def bus_manage(interval=5, r_num=1, current_hour=0):  # управление числом автобусов на маршруте
    num_day = datetime.datetime.today().isoweekday()
    day_idx = 0
    if num_day < 6:
        day_idx = 0
    else:
        day_idx = 1
    rout_num = len(rout_dict)  # количество марщрутов

    i = 0
    for n_rout in rout_dict:  # вычисление ключа маршрута в словаре
        if str(rout_dict[n_rout]) == r_num:
            break
        i += 1
    route_len = routs_info['Длинна маршрута, км'][i]  # длина маршрута
    stop_num = routs_info['Количество остановок'][i]  # количество остановок

    thread_per_route = passenger_thread[day_idx][current_hour] / rout_num  # пассажиропоток на маршрут на час
    t_in_route = (2 * route_len) / BUS_SPEED + 2 * STOP_TIME * stop_num + REST_TIME  # время автобуса в пути
    ppl_in_interval = (thread_per_route * (interval + STOP_TIME)) / 60  # пассажиропоток на интервал на одном маршруте

    n_big = 0  # количество больших автобусов
    n_min = t_in_route / interval  # количество маленьких автобусов
    while True:
        n = t_in_route/interval
        if (n_min*PAS_CAP_MIN+n_big*PAS_CAP_MAX)*0.8 < ppl_in_interval:  # меняем маленькие автобусы на большие, если общая пассажировместимость на маршруте не может удовлетворить пассажиропоток
            n_min-=1
            n_big+=1
        else:
            break
    return [n_min, n_big]




# def get_max_p_t_per_hour():
#
#     max = 0
#     for cur_h in range(1, 24):
#         thread_per_route = PASSENGER_THREAD[cur_h] / ROUTE_NUM
#         if max < thread_per_route:
#             max = thread_per_route
#     print('Max = ', max)

#bus_manage()