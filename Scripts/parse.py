import json
import os


class Parse:
    def __init__(self, path):
        # folder_path - Путь к папке с JSON-файлами
        self.main_folder_path = path

        '''
        DB.Metrics.Status - состояние MySQL. SHOW GLOBAL STATUS
        DB.Metrics.Latency - Latency в момент сбора
        DB.Conf - полная конфигурация MySQL
        System - информация о система CPU, Memory
        '''

        self.db_metrics_status = []
        self.db_metrics_latency = []
        self.db_conf = []
        self.system = []
        self.global_arr = []

    @staticmethod
    def is_numeric(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def read_mining(self):
        # Получаем список папок
        folders_list = os.listdir(self.main_folder_path)
        folders_list.remove('.idea')

        # Проходимся по каждой папке
        for folder_name in folders_list:
            # Формируем полный путь к файлу
            files_list = os.listdir(self.main_folder_path + f'/{folder_name}')

            print(folder_name)

            # Проходим по каждому json'у
            for file_name in files_list:
                file_path = self.main_folder_path + f'/{folder_name}' + f'/{file_name}'
                # print(file_path)

                # Проверяем, является ли файл JSON-файлом
                if file_name.endswith('.json'):
                    # Открываем JSON-файл для чтения
                    with open(file_path, 'r') as file:
                        # Загружаем JSON-данные
                        json_data = json.load(file)

                        # Проверяем, присутствует ли ключ в JSON-данных
                        if 'DB' and 'System' in json_data:
                            if json_data['DB']['Metrics']['Latency'] is not None:

                                hashes = {}
                                for key, value in json_data['DB']['Metrics']['Status'].items():
                                    if value is not None and self.is_numeric(value):
                                        hashes[key] = float(value)
                                # Status
                                self.db_metrics_status.append(hashes)

                                hashes = {}
                                for value in json_data['DB']['Metrics']['Latency']:
                                    if value is not None and self.is_numeric(value):
                                        hashes['Latency'] = float(value)
                                # Latency
                                self.db_metrics_latency.append(hashes)

                                hashes = {}
                                for key, value in json_data['DB']['Conf']['Variables'].items():
                                    if value is not None and self.is_numeric(value):
                                        hashes[key] = float(value)
                                # Config
                                self.db_conf.append(hashes)
                                # System info(not using)
                                # self.system.append(json_data['System'])
                                self.global_arr.append([self.db_metrics_status, self.db_metrics_latency, self.db_conf, self.system])

        return self.global_arr
