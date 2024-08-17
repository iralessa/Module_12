import unittest
import logging
from rt_with_exceptions import Runner  # Импортируем класс Runner из модуля rt_with_exceptions

# Настройка логирования
logging.basicConfig(filename='runner_tests.log',
                    level=logging.INFO,
                    filemode='w',
                    encoding='utf-8',
                    format=' | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        name = "Иван"
        try:
            # Попытка создать объект с отрицательной скоростью
            runner = Runner(name, -5)

        except ValueError as e:
            logging.warning("Неверный тип данных для бегуна '%s' | %s", name, e)
        else:
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        name = 12345
        try:
            # Попытка создать объект с некорректным типом имени int
            runner = Runner(name, 10)
        except TypeError as e:
            logging.warning("Неверный тип данных для имени '%s' | %s",name, e)
        else:
            logging.info('"test_run" выполнен успешно')


if __name__ == '__main__':
    unittest.main()