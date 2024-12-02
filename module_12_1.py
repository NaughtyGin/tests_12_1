import unittest
import runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        test_obj = runner.Runner('Someone')
        for i in range(10):
            test_obj.walk()
        self.assertEqual(50, test_obj.distance)

    def test_run(self):
        test_obj = runner.Runner('Someone')
        for i in range(10):
            test_obj.run()
        self.assertEqual(100, test_obj.distance)

    def test_challenge(self):
        test_obj_1 = runner.Runner('First')
        test_obj_2 = runner.Runner('Second')
        for i in range(10):
            test_obj_1.walk()
            test_obj_2.run()
        print(f'First distance: {test_obj_1.distance}')
        print(f'Second distance: {test_obj_2.distance}')
        self.assertNotEqual(test_obj_1.distance, test_obj_2.distance)


if __name__ == '__main__':
    unittest.main()
