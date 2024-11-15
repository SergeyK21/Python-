"""
Дан файл системы контроля спорткомплекса. Вам нужно:

 - Прочитать файл (поля в файле разделены символом табуляции «\t»).
 - Вычислить время, проведённое спортсменом в бассейне (разница между временем входа и выхода из бассейна).
 - Рассчитать время, проведённое в комплексе (время между входом и выходом в комплекс).
 - Вывести в отдельный файл с логами в случае, если данные о выходе спортсмена отсутствуют,
    а также в случае обнаружения ошибок или неточностей в записях
    (отсутствие времени входа, выхода, противоречия в записях).
"""
from  datetime import datetime
import pprint
import copy as cp
import math

import logging

logger1 = logging.getLogger('Athlete')
logger1.setLevel(logging.INFO)

logger2 = logging.getLogger('ERROR')
logger2.setLevel(logging.DEBUG)

ch = logging.FileHandler(
    filename="./file_ex_8/Athlete.txt",
    mode='w',
    encoding='utf-8'
)
ch.setLevel(logging.INFO)

fh = logging.FileHandler(
    filename="./file_ex_8/logs.log",
    mode='w',
    encoding='utf-8'
)
fh.setLevel(logging.DEBUG)

formatter1 = logging.Formatter('%(message)s')
formatter2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter1)
fh.setFormatter(formatter2)

logger1.addHandler(ch)
logger2.addHandler(fh)


data_file_dict = {}
check_list = []



with open('./file_ex_8/activity.csv', 'r') as f:
    fl = True # Флаг строки заголовка
    for line in f:
        # Строка заголовка (дата, атлет, локация, Присутствие/отсутствие)
        if fl:
            for el in line.replace('\n', '').replace('/', '-').split(sep=','):
                data_file_dict[el]=[]
            fl = False
            continue
        # Добавление файлов в data_file_dict согласно строке заголовка
        generator = (data_file_dict.keys().__iter__())
        # print(line)
        fl2 = True
        for el in line.replace('\n', '').replace('/', '-').split(sep=','):

            #print(el)
            try:
                if fl2:
                    data_file_dict[generator.__next__()].append(datetime.strptime(el, "%d-%m-%Y %H:%M:%S"))
                    fl2 = False
                elif el.isdigit():
                    data_file_dict[generator.__next__()].append(int(el))
                else:
                    data_file_dict[generator.__next__()].append(el)
            except StopIteration as ex:
                break

ID = {} # Идентификатор атлета
# pprint.pp(data_file_dict)

temp_dict_type = {} # присутствие/отсутствие

for el in list(set(data_file_dict[list(data_file_dict.keys())[3]])):
    temp_dict_type[el] = None

temp_dict_loc = {} # локация

for el in list(set(data_file_dict[list(data_file_dict.keys())[2]])):
    temp_dict_loc[el] = cp.deepcopy(temp_dict_type)

for el in list(set(data_file_dict[list(data_file_dict.keys())[1]])):
    ID[el] = cp.deepcopy(temp_dict_loc)


data_list_date = data_file_dict[list(data_file_dict.keys())[0]]
data_list_id = data_file_dict[list(data_file_dict.keys())[1]]
data_list_loc = data_file_dict[list(data_file_dict.keys())[2]]
data_list_type = data_file_dict[list(data_file_dict.keys())[3]]


for i in range(len(data_list_id)):
    for key_type in ID[data_list_id[i]][data_list_loc[i]].keys():
        if key_type == data_list_type[i]:
            if ID[data_list_id[i]][data_list_loc[i]][key_type] is None:
                ID[data_list_id[i]][data_list_loc[i]][key_type] = []
            ID[data_list_id[i]][data_list_loc[i]][key_type].append(data_list_date[i])
            break

for id in ID.keys():
    for loc in ID[id]:
        try:
            if ID[id][loc]["Out"] == None and ID[id][loc]["In"] != None:
                if isinstance(ID[id][loc]["In"], list):
                    logger2.debug(f"Не зафиксировано время выхода атлета {id} из {loc}")
                else:
                    raise Exception("Ошибка!")
            elif ID[id][loc]["Out"] != None and ID[id][loc]["In"] == None:
                if isinstance(ID[id][loc]["Out"], list):
                    logger2.debug(f"Не зафиксировано время входа атлета {id} из {loc}")
                else:
                    raise Exception("Ошибка!")
            elif ID[id][loc]["Out"] != None and ID[id][loc]["In"] != None:
                if isinstance(ID[id][loc]["In"], list) and isinstance(ID[id][loc]["In"], list):
                    if len(ID[id][loc]["In"]) == len(ID[id][loc]["Out"]):
                        el = zip(ID[id][loc]["Out"], ID[id][loc]["In"])
                        for i in el:
                            min = math.ceil((i[0] - i[1]).total_seconds() / 60)
                            if i[0] == i[1]:
                                min = 0
                            logger1.info(f'Атлет {id} провёл в {loc}: {min}')\
                                if min > 0 \
                                else logger2.debug(f"Не зафиксировано время входа атлета {id} из {loc}")
                    elif len(ID[id][loc]["In"]) > len(ID[id][loc]["Out"]):
                        el = zip(ID[id][loc]["Out"], ID[id][loc]["In"])
                        for i in el:
                            min = math.ceil((i[0] - i[1]).total_seconds() / 60)
                            if i[0] == i[1]:
                                min = 0
                            logger1.info(f'Атлет {id} провёл в {loc}: {min}')\
                                if min > 0 \
                                else logger2.debug(f"Не зафиксировано время входа атлета {id} из {loc}")
                        for i in range(len(ID[id][loc]["Out"]) - 1, len(ID[id][loc]["In"])):
                            logger2.debug(f"Не зафиксировано время выхода атлета {id} из {loc}")
                    elif len(ID[id][loc]["In"]) < len(ID[id][loc]["Out"]):
                        el = zip(ID[id][loc]["Out"], ID[id][loc]["In"])
                        for i in el:
                            min = math.ceil((i[0] - i[1]).total_seconds() / 60)
                            if i[0] == i[1]:
                                min = 0
                            logger1.info(f'Атлет {id} провёл в {loc}: {min}')\
                                if min > 0 \
                                else logger2.debug(f"Не зафиксировано время входа атлета {id} из {loc}")
                        for i in range(len(ID[id][loc]["In"]) - 1, len(ID[id][loc]["Out"])):
                            logger2.debug(f"Не зафиксировано время входа атлета {id} из {loc}")
                else:
                    raise Exception("Ошибка!")
        except Exception as ex:
            logger2.debug(f'{ex}')

pprint.pp(ID)
