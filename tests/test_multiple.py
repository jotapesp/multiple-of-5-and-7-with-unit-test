import pytest
from functions import multiple_five, multiple_seven, if_not_multiple_seven_and_five

class TestMultipleFiveAndSeven:
    def setup_method(self):
        pass

    def test_multiple_five(self):
        output = multiple_five(10)
        assert output == 'fizz'

    def test_multiple_seven(self):
        output = multiple_seven(14)
        assert output == 'buzz'

    def test_not_multiple(self):
        output = if_not_multiple_seven_and_five(31)
        assert output == 'miss'
