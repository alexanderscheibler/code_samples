import pytest

from .reformat_date import reformat_date


def test_reformat_date_valid_single_date():
    """Test a valid single date input."""
    dates = ['25th May 1912']
    expected = ['1912-05-25']
    assert reformat_date(dates) == expected

def test_reformat_date_multiple_valid_dates():
    """Test multiple valid dates."""
    dates = ['25th May 1912', '16th Dec 2018', '26th Dec 2061']
    expected = ['1912-05-25', '2018-12-16', '2061-12-26']
    assert reformat_date(dates) == expected

def test_reformat_date_leap_year():
    """Test leap year date handling."""
    dates = ['29th Feb 2020']  # 2020 is a leap year
    expected = ['2020-02-29']
    assert reformat_date(dates) == expected

def test_reformat_date_non_leap_year():
    """Test non-leap year February 29 should raise an error."""
    dates = ['29th Feb 2019']  # 2019 is not a leap year
    with pytest.raises(ValueError):
        reformat_date(dates)

def test_reformat_date_invalid_day_suffix():
    """Test a date with an invalid day suffix."""
    dates = ['23rdx Jan 2020']
    with pytest.raises(ValueError):
        reformat_date(dates)

def test_reformat_date_empty_day_suffix():
    """Test a date with an empty day suffix."""
    dates = ['23 Jan 2020']
    with pytest.raises(ValueError):
        reformat_date(dates)

def test_reformat_date_invalid_month():
    """Test a date with an invalid month."""
    dates = ['15th Foo 2021']
    with pytest.raises(ValueError):
        reformat_date(dates)

def test_reformat_date_empty_month():
    """Test a date with an empty month."""
    dates = ['15th 2021']
    with pytest.raises(ValueError):
        reformat_date(dates)

def test_reformat_date_invalid_year_not_numeric():
    """Test a date with an invalid year."""
    dates = ['15th Dec abcd']
    with pytest.raises(ValueError):
        reformat_date(dates)

def test_reformat_date_empty_string():
    """Test an empty date string."""
    dates = ['']
    with pytest.raises(ValueError):
        reformat_date(dates)

def test_reformat_date_empty_list():
    """Test an empty list of dates."""
    dates = []
    expected = []
    assert reformat_date(dates) == expected

def test_reformat_date_mixed_valid_and_invalid_dates():
    """Test a mix of valid and invalid dates."""
    dates = ['1st Jan 2021', 'Invalid Date', '15th Mar 2015']
    with pytest.raises(ValueError):
        reformat_date(dates)

def test_reformat_date_already_ISO_format():
    """Test a completely invalid date format."""
    dates = ['2021-01-01']
    with pytest.raises(ValueError):
        reformat_date(dates)

def test_reformat_date_edge_case_before_first_day_of_year():
    """Test before the first day of the year."""
    dates = ['00th Jan 2023']
    with pytest.raises(ValueError):
        reformat_date(dates)

def test_reformat_date_edge_case_first_day_of_year():
    """Test the first day of the year."""
    dates = ['1st Jan 2023']
    expected = ['2023-01-01']
    assert reformat_date(dates) == expected

def test_reformat_date_edge_case_last_day_of_year():
    """Test the last day of the year."""
    dates = ['31st Dec 2023']
    expected = ['2023-12-31']
    assert reformat_date(dates) == expected

def test_reformat_date_edge_case_beyond_last_day_of_year():
    """Test after the last day of the year."""
    dates = ['32st Dec 2023']
    with pytest.raises(ValueError):
        reformat_date(dates)

def test_reformat_date_edge_case_31st_in_months_with_30_days():
    """Test a date where 31st is used in a month with only 30 days."""
    dates = ['31st Apr 2021']  # April only has 30 days
    with pytest.raises(ValueError):
        reformat_date(dates)

def test_reformat_date_edge_case_february_30():
    """Test February 30th, which is always invalid."""
    dates = ['30th Feb 2021']
    with pytest.raises(ValueError):
        reformat_date(dates)

def test_reformat_date_strip_whitespace():
    """Test that leading/trailing whitespace is handled correctly."""
    dates = ['   1st Jan 2023   ']
    expected = ['2023-01-01']
    assert reformat_date(dates) == expected

def test_reformat_date_case_insensitive_month():
    """Test that month names are case-insensitive."""
    dates = ['1st JAN 2023', '2nd feb 2024', '3rd Mar 2025']
    expected = ['2023-01-01', '2024-02-02', '2025-03-03']
    assert reformat_date(dates) == expected

def test_reformat_date_invalid_input_type_with_integers_not_string():
    """Test invalid input type (e.g., int instead of string)."""
    dates = [12345]
    with pytest.raises(TypeError):
        reformat_date(dates)