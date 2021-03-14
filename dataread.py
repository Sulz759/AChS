# -*- coding: utf-8 -*-

def data_read(path_to_data):
    # функция чтения данных из файла

    znachenye_one_list = []
    znachenye_two_list= []
    znone_zntwo = []

    input_file = open(path_to_data, 'r', encoding='utf-8')
    red_data = input_file.readline()
    red_data = (red_data.replace('\n','')).split('\t')

    if len(red_data) > 0:
        for line in input_file.readlines():
            row = (line.replace('\n','')).split('\t')
            for position in range(len(row)):
                if position == red_data.index('Время'):
                    znachenye_one_list.append(float(row[position]))
                if position == red_data.index('ТМИ'):
                    znachenye_two_list.append(float(row[position]))


    znone_zntwo.append(znachenye_one_list)
    znone_zntwo.append(znachenye_two_list)

    return znone_zntwo

