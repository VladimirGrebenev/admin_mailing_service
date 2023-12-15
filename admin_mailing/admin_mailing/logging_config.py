import logging
import os

# путь к файлу логирования
file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'app.log')

# Создание объекта логгера
logger = logging.getLogger('main_app' + __name__)
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи в файл
file_handler = logging.FileHandler(file_path)  # Замените file_path на путь к файлу логов
file_handler.setLevel(logging.DEBUG)

# Создание обработчика для вывода в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Создание форматтера
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

# Привязка форматтера к обработчикам
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Добавление обработчиков к логгеру
logger.addHandler(file_handler)
logger.addHandler(console_handler)