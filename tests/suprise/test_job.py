import pytest
from suprise.job import Job


class TestJob:
    @pytest.fixture(autouse=True)
    def _constants(self, test_add_numbers):
        self.test_number, self.test_result = test_add_numbers

    def test_addition(self):
        result = Job.addition(*self.test_number)
        assert result == self.test_result
