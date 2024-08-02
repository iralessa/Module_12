from Runner import Runner  # Импортируем класс Runner из модуля Runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        # Создаем объект Runner с произвольным именем
        runner = Runner("Иван")

        # Вызываем метод walk 10 раз
        for i in range(10):
            runner.walk()

        # Проверяем, что distance равен 50 у конкретного объекта runner
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        # Создаем объект Runner с произвольным именем
        runner = Runner("Роман")

        # Вызываем метод run 10 раз
        for i in range(12):
            runner.run()

        # Проверяем, что distance равен 100 у конкретного объекта runner
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        # Создаем два объекта Runner с произвольными именами
        runner1 = Runner("София")
        runner2 = Runner("Ольга")

        # Вызываем методы run и walk 10 раз у каждого объекта
        for i in range(10):
            runner1.run()
            runner2.walk()

        # Проверяем, что distance у объектов не равны между собой
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()