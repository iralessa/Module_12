import unittest
from Runner import Runner
from runner_and_tournament import Runner
from runner_and_tournament import Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        # Создаем объект Runner с произвольным именем
        runner = Runner("Иван")

        # Вызываем метод walk 10 раз
        for i in range(10):
            runner.walk()

        # Проверяем, что distance равен 50 у конкретного объекта runner
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        # Создаем объект Runner с произвольным именем
        runner = Runner("Роман")

        # Вызываем метод run 10 раз
        for i in range(10):
            runner.run()

        # Проверяем, что distance равен 100 у конкретного объекта runner
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
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


class TournamentTest(unittest.TestCase):
    is_frozen = True

#setUpClass — это метод, который вызывается один раз перед запуском всех тестов в этом классе
    @classmethod
    def setUpClass(cls): # метод получает доступ к самому классу через параметр cls
        cls.all_results = {}  # словарь предназначен для хранения результатов

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self): # метод вызывается перед каждым тестом, создаются 3 объекта
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)


    @classmethod
    def tearDownClass(cls): #метод, который вызывается один раз после завершения всех тестов
        #выводятся все результаты, которые были сохранены в словаре all_results в процессе выполнения тестов
        print("\nВсе результаты:")
        for test_name, result in cls.all_results.items():
            print(f"{test_name}: {result}")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_U_N(self): #метод тестирует турнир, в котором участвуют Усэйн и Ник
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        TournamentTest.all_results['test_U_N'] = {place: runner.name for place, runner in results.items()}
        last_place_runner = results[max(results.keys())]
        self.assertTrue(last_place_runner == "Ник") #Ник занимает последнее место

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_A_N(self): #метод тестирует турнир, в котором участвуют Андрей и Ник
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results['test_A_N'] = {place: runner.name for place, runner in results.items()}
        last_place_runner = results[max(results.keys())]
        self.assertTrue(last_place_runner == "Ник") #Ник занимает последнее место

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_U_A_N(self): #тест включает всех трех участников: Усэйна, Андрея и Ника
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results['test_U_A_N'] = {place: runner.name for place, runner in results.items()}
        last_place_runner = results[max(results.keys())]
        self.assertTrue(last_place_runner == "Ник") #Ник занимает последнее место

if __name__ == "__main__":
    unittest.main()
