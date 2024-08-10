class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
# # Создаем объекты бегунов
# runner1 = Runner("Усэйн", 10)
# runner2 = Runner("Андрей", 9)
# runner3 = Runner("Ник", 3)
#
# # Создаем объект турнира
# tournament = Tournament(9, runner1, runner2, runner3)
#
# # Запускаем турнир
# results = tournament.start()
#
# # Выводим результаты на экран
# print("Результат турнира:")
# for place, runner in results.items():
#     print(f"{place}-е место: {runner.name}, пройденное расстояние: {runner.distance}, скорость: {runner.speed}")