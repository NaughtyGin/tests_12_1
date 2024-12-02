import unittest
import rt_with_exceptions
import runner_and_tournament


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        test_obj = rt_with_exceptions.Runner('Someone')
        for i in range(10):
            test_obj.walk()
        self.assertEqual(50, test_obj.distance)

    def test_run(self):
        test_obj = rt_with_exceptions.Runner('Someone')
        for i in range(10):
            test_obj.run()
        self.assertEqual(100, test_obj.distance)

    def test_challenge(self):
        test_obj_1 = rt_with_exceptions.Runner('First', 5)
        test_obj_2 = rt_with_exceptions.Runner('Second', 5)  # установить speed != 5
        if test_obj_1.speed != test_obj_2.speed:
            test_challenge_objs = [test_obj_1, test_obj_2]
        else:
            raise ValueError(f'Скорость участников не может быть одинаковой, сейчас они равны: '
                             f'{test_obj_1.speed == test_obj_2.speed}')
        for test_obj in test_challenge_objs:
            for i in range(10):
                test_obj.walk()
                test_obj.run()
        print(f'First distance: {test_obj_1.distance}')
        print(f'Second distance: {test_obj_2.distance}')
        self.assertNotEqual(test_obj_1.distance, test_obj_2.distance)

if __name__ == '__main__':
    unittest.main()