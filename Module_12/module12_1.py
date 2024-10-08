import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r1 = runner.Runner('Mike')
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    def test_run(self):
        r2 = runner.Runner('Alex')
        for i in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)

    def test_challenge(self):
        r1 = runner.Runner('Mike')
        r2 = runner.Runner('Alex')
        for i in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)