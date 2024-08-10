import unittest
from runner_and_tournament import Runner
from runner_and_tournament import Tournament
class TournamentTest(unittest.TestCase):

#setUpClass — это метод, который вызывается один раз перед запуском всех тестов в этом классе
    @classmethod
    def setUpClass(cls): # метод получает доступ к самому классу через параметр cls
        cls.all_results = {}  # словарь предназначен для хранения результатов

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
    def test_U_N(self): #метод тестирует турнир, в котором участвуют Усэйн и Ник
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        TournamentTest.all_results['test_U_N'] = {place: runner.name for place, runner in results.items()}
        last_place_runner = results[max(results.keys())]
        self.assertTrue(last_place_runner == "Ник") #Ник занимает последнее место


    def test_A_N(self): #метод тестирует турнир, в котором участвуют Андрей и Ник
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results['test_A_N'] = {place: runner.name for place, runner in results.items()}
        last_place_runner = results[max(results.keys())]
        self.assertTrue(last_place_runner == "Ник") #Ник занимает последнее место


    def test_U_A_N(self): #тест включает всех трех участников: Усэйна, Андрея и Ника
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results['test_U_A_N'] = {place: runner.name for place, runner in results.items()}
        last_place_runner = results[max(results.keys())]
        self.assertTrue(last_place_runner == "Ник") #Ник занимает последнее место

if __name__ == "__main__":
    unittest.main()
