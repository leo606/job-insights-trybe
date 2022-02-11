import pytest
from src.sorting import sort_by

jobs = [
    {"max_salary": 0, "min_salary": 10, "date_posted": "2020-04-20"},
    {"max_salary": 10, "min_salary": 100, "date_posted": "2020-04-21"},
    {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-04-22"},
    {"max_salary": 15000, "min_salary": 4, "date_posted": "2020-04-23"},
    {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-04-24"},
    {"max_salary": -1, "min_salary": 10, "date_posted": "2020-04-25"},
]

criterias = ("min_salary", "max_salary", "date_posted")


def test_sort_by_criteria():
    with pytest.raises(ValueError, match="invalid sorting criteria: invalid"):
        assert sort_by(jobs, criteria="invalid")
