import pandas
import xlrd

class City(object):
    passengers_thread_w = []
    passengers_thread_h = []
    population = 0
    population_with_cars = 0
    transport_index = 0 #Индекс людей без личного транспорта
    index_passengers_thread_w = []
    index_passengers_thread_h = []

    def __init__(self):
        pass

    def set_passenger_thread_w(self, data):
        self.passengers_thread_w.extend(data)

    def set_passenger_thread_h(self, data):
        self.passengers_thread_h.extend(data)


    def set_population(self, data):
        self.population = data


    def set_population_with_cars(self, data):
        self.population_with_cars = data


    def configure_city(self, population, population_w_cars):
        self.transport_index = self.population/(1-self.population_with_cars)
        for data in self.passengers_thread_w:
            self.index_passengers_thread_w.append(data/self.population)
        for data in self.passengers_thread_h:
            self.index_passengers_thread_h.append(data/self.population)


def Get_passengers_thread_in_day():
    xlsxDatapop = pandas.read_excel("population_info_in_our_city.xlsx")
    population = xlsxDatapop.to_dict()['Население'][0]
    population_w_cars = xlsxDatapop.to_dict()['Население с автомобилями'][0]
    #Считана информация о населении
    xlsxData = pandas.read_excel("cities_info.xlsx")
    cities = []
    rows = xlsxData.index.stop
    p_t_list_w = []
    p_t_list_h = []
    for i in range(0, rows, 4):
        for j in range(1, 25):
             p_t_list_w.append(xlsxData[j][i])
        for j in range(1, 25):
             p_t_list_h.append(xlsxData[j][i+1])
        populat = xlsxData[1][i+2]
        populat_w_cars = xlsxData[1][i+3]
        city = City
        city.set_passenger_thread_w(city, p_t_list_w)
        city.set_passenger_thread_h(city, p_t_list_h)
        city.set_population(city, populat)
        city.set_population_with_cars(city, populat_w_cars)
        city.configure_city(city, population, population_w_cars)
        cities.append(city)
    #Считана информация о городах из файла excel
    sum_coeff_w = [0 for i in range(24)]
    sum_coeff_h = [0 for i in range(24)]
    for city in cities:
        i = 0
        for coeff in city.index_passengers_thread_w:
            sum_coeff_w[i] += coeff
            i += 1
        i = 0
        for coeff in city.index_passengers_thread_h:
            sum_coeff_h[i] += coeff
            i += 1
    for i in range(24):
        sum_coeff_w[i] /= len(cities)
        sum_coeff_h[i] /= len(cities)
    passenger_thread_for_day_w = []
    passenger_thread_for_day_h = []
    for coeff in sum_coeff_w:
        passenger_thread_for_day_w.append(coeff*(int(population-populat_w_cars)))
    for coeff in sum_coeff_h:
        passenger_thread_for_day_h.append(coeff*(int(population-populat_w_cars)))
    return [passenger_thread_for_day_w, passenger_thread_for_day_h] #Пассажиропоток в рабочие дни + в выходные


def Get_routs_info():
    xlsxData = pandas.read_excel('Dannye_po_marshrutam.xlsx')
    data_as_dict = xlsxData.to_dict()
    return data_as_dict








