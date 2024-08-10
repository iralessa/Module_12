# 1 часть
import unittest
import TournamentTest
import RunnerTest
runST = unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(runST)
TournamentST = unittest.TestSuite()
TournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(TournamentST)

# 2 часть