import unittest


class PersonalTest(unittest.TestCase):
    def setUp(self):
        return True

    def test_today_count(self):
        assert True

    def test_news(self):
        self.getTitleByNumber(4)

    def getTitleByNumber(self, number):
        assert number == 4

    def tear_down(self):
        return True


if __name__ == "__main__":
    unittest.main()

