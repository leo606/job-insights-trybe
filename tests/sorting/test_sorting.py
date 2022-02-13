import pytest
from src.sorting import sort_by

MOCK_JOBS = [
    {"max_salary": 0, "min_salary": 10, "date_posted": "2020-04-20"},
    {"max_salary": 10, "min_salary": 100, "date_posted": "2020-04-21"},
    {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-04-22"},
    {"max_salary": 15000, "min_salary": 4, "date_posted": "2020-04-23"},
    {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-04-24"},
]

MOCK_JOBS_BY_MIN_SALARAY = [
    {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-04-24"},
    {"max_salary": 15000, "min_salary": 4, "date_posted": "2020-04-23"},
    {"max_salary": 0, "min_salary": 10, "date_posted": "2020-04-20"},
    {"max_salary": 10, "min_salary": 100, "date_posted": "2020-04-21"},
    {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-04-22"},
]

MOCK_JOBS_BY_MAX_SALARY = [
    {"max_salary": 15000, "min_salary": 4, "date_posted": "2020-04-23"},
    {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-04-22"},
    {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-04-24"},
    {"max_salary": 10, "min_salary": 100, "date_posted": "2020-04-21"},
    {"max_salary": 0, "min_salary": 10, "date_posted": "2020-04-20"},
]

MOCK_JOBS_BY_DATE = [
    {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-04-24"},
    {"max_salary": 15000, "min_salary": 4, "date_posted": "2020-04-23"},
    {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-04-22"},
    {"max_salary": 10, "min_salary": 100, "date_posted": "2020-04-21"},
    {"max_salary": 0, "min_salary": 10, "date_posted": "2020-04-20"},
]

criterias = ("min_salary", "max_salary", "date_posted", "invalid")


def test_sort_by_criteria():
    sort_by_min_salary = MOCK_JOBS
    sort_by(sort_by_min_salary, criterias[0])
    assert sort_by_min_salary == MOCK_JOBS_BY_MIN_SALARAY

    sort_by_max_salary = MOCK_JOBS
    sort_by(sort_by_max_salary, criterias[1])
    assert sort_by_max_salary == MOCK_JOBS_BY_MAX_SALARY

    sort_by_date = MOCK_JOBS
    sort_by(sort_by_date, criterias[2])
    assert sort_by_date == MOCK_JOBS_BY_DATE

    with pytest.raises(ValueError, match="invalid sorting criteria: invalid"):
        assert sort_by(MOCK_JOBS, criterias[3])
