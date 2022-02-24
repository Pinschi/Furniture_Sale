import pytest
from decimal import Decimal
from datetime import date
from Furniture_sale import calculate_discount

# Arrange

_test_data_outside_advent_season =[
    pytest.param( date(2022, 11, 25), Decimal('63.75'), Decimal('0.00'), id="TC1 - 0% discount outside advent period"),
    pytest.param( date(2022, 12, 27), Decimal('63.75'), Decimal('0.00'), id="TC2 - 0% discount outside advent period")]

_test_data_inside_advent_season =[
    pytest.param( date(2022, 11, 28), Decimal('0.01'), Decimal('0.05'), id="TC3 - 5 % discount inside advent period  with 0 < total < 100"),
    pytest.param( date(2022, 11, 28), Decimal('99.99'), Decimal('0.05'), id="TC4 - 5 % discount inside advent period  with 0 < total < 100"),
    pytest.param( date(2022, 12, 7), Decimal('0.01'), Decimal('0.05'), id="TC5 - 5 % discount inside advent period  with 0 < total < 100"),
    pytest.param( date(2022, 12, 7), Decimal('99.99'), Decimal('0.05'), id="TC6 - 5 % discount inside advent period  with 0 < total < 100"),
    pytest.param( date(2022, 12, 23), Decimal('0.01'), Decimal('0.05'), id="TC7 - 5 % discount inside advent period  with 0 < total < 100"),
    pytest.param( date(2022, 12, 23), Decimal('99.99'), Decimal('0.05'), id="TC6 - 5 % discount inside advent period  with 0 < total < 100"),
    pytest.param( date(2022, 11, 28), Decimal('100'), Decimal('0.1'),id="TC9 - 10 % discount inside advent period  with 50 =< total < 100"),
    pytest.param( date(2022, 11, 28), Decimal('100.01'), Decimal('0.1'),id="TC10 - 10 % discount inside advent period  with 50 =< total < 100"),
    pytest.param( date(2022, 11, 28), Decimal('499.99'), Decimal('0.1'),id="TC11 - 10 % discount inside advent period  with 50 =< total < 100"),
    pytest.param( date(2022, 12, 7), Decimal('100'), Decimal('0.1'),id="TC12 - 10 % discount inside advent period  with 50 =< total < 100"),
    pytest.param( date(2022, 12, 7), Decimal('100.01'), Decimal('0.1'),id="TC13 - 10 % discount inside advent period  with 50 =< total < 100"),
    pytest.param( date(2022, 12, 7), Decimal('499.99'), Decimal('0.1'),id="TC14 - 10 % discount inside advent period  with 50 =< total < 100"),
    pytest.param( date(2022, 12, 23), Decimal('100'), Decimal('0.1'),id="TC15 - 10 % discount inside advent period  with 50 =< total < 100"),
    pytest.param( date(2022, 12, 23), Decimal('100.01'), Decimal('0.1'),id="TC16 - 10 % discount inside advent period  with 50 =< total < 100"),
    pytest.param( date(2022, 12, 23), Decimal('499.99'), Decimal('0.1'),id="TC17 - 10 % discount inside advent period  with 50 =< total < 100"),
    pytest.param( date(2022, 11, 28), Decimal('500'), Decimal('0.2'),id="TC18 - 20 % discount inside advent period  with 500 =< total"),
    pytest.param( date(2022, 11, 28), Decimal('500.01'), Decimal('0.2'),id="TC19 - 20 % discount inside advent period  500 =< total"),
    pytest.param( date(2022, 12, 7), Decimal('500.00'), Decimal('0.2'),id="TC20 - 20 % discount inside advent period   500 =< total"),
    pytest.param( date(2022, 12, 7), Decimal('500.01'), Decimal('0.2'),id="TC21 - 20 % discount inside advent period   500 =< total"),
    pytest.param( date(2022, 12, 23), Decimal('500.00'), Decimal('0.2'),id="TC22 - 20 % discount inside advent period   500 =< total"),
    pytest.param( date(2022, 12, 23), Decimal('500'), Decimal('0.2'),id="TC23- 20 % discount inside advent period   500 =< total")]

_test_saturdays_inside_advent_season =[
    pytest.param( date(2022, 11, 26), Decimal('0.01'), Decimal('0.15'), id="TC24 - 5 % + 10% discount inside advent period on Saturdays with 0 < total < 100"),
    pytest.param( date(2022, 11, 26), Decimal('99.99'), Decimal('0.15'), id="TC25 - 5 % + 10% discount inside advent period on Saturdays with 0 < total < 100"),
    pytest.param( date(2022, 12, 24), Decimal('0.01'), Decimal('0.15'), id="TC26 - 5 % + 10% discount inside advent period on Saturdays with 0 < total < 100"),
    pytest.param( date(2022, 12, 24), Decimal('99.99'), Decimal('0.15'), id="TC27 - 5 % + 10% discount inside advent period on Saturdays with 0 < total < 100"),
    pytest.param(date(2022, 11, 26), Decimal('100'), Decimal('0.19'), id="TC28 - 10 % + 10% discount inside advent period on Saturdays with 50 =< total < 100"),
    pytest.param(date(2022, 11, 26), Decimal('100.01'), Decimal('0.19'),id="TC29 - 10 % + 10% discount inside advent period on Saturdays with 50 =< total < 100"),
    pytest.param(date(2022, 11, 26), Decimal('499.99'), Decimal('0.19'),id="TC30 - 10 % + 10% discount inside advent period on Saturdays with 50 =< total < 100"),
    pytest.param(date(2022, 12, 24), Decimal('100'), Decimal('0.19'), id="TC31 - 10 % + 10% discount inside advent period on Saturdays with 50 =< total < 100"),
    pytest.param(date(2022, 12, 24), Decimal('100.01'), Decimal('0.19'),id="TC32 - 10 % + 10% discount inside advent period on Saturdays with 50 =< total < 100"),
    pytest.param(date(2022, 12, 24), Decimal('499.99'), Decimal('0.19'), id="TC33 - 10 % + 10% discount inside advent period on Saturdays with 50 =< total < 100"),
    pytest.param( date(2022, 11, 26), Decimal('500'), Decimal('0.28'),id="TC34 - 20 % + 10% discount inside advent period on Saturdays with 500 =< total"),
    pytest.param( date(2022, 11, 26), Decimal('500.01'), Decimal('0.28'),id="TC35 - 20 % + 10% discount inside advent period on Saturdays with 500 =< total"),
    pytest.param( date(2022, 12, 24), Decimal('500.00'), Decimal('0.28'),id="TC36 - 20 % + 10% discount inside advent period on Saturdays with 500 =< total"),
    pytest.param( date(2022, 12, 24), Decimal('500.01'), Decimal('0.28'),id="TC37 - 20 % + 10% discount inside advent period on Saturdays with 500 =< total")]

_test_data_advent_season_robustness =[
    pytest.param( date(2022, 11, 27), Decimal('0.01'),  id="TC38 - Sunday, inside advent => ValueError"),
    pytest.param( date(2022, 12, 8), Decimal('99.99'), id="Holiday, inside advent => ValueError"),
    pytest.param( date(2022, 12, 18), Decimal('0.01'),  id="TC40 -  Sunday, inside advent => ValueError"),
    pytest.param( date(2022, 12, 25), Decimal('99.99'),  id="Holiday, inside advent => ValueError"),
    pytest.param( date(2022, 12, 26), Decimal('0.01'),  id="Holiday, inside advent => ValueError"),
    pytest.param(8.23, Decimal('99.99'),  id="TC43 - day not a date ==> ValueError"),
    pytest.param( date(2022, 11, 28), Decimal('0'),id="TC44 - total = 0 "),
    pytest.param( date(2022, 11, 28),  Decimal('-0.01'),id="TC45 - total negative value"),
    pytest.param(date(2022, 11, 28),"abc", id="TC46 - total not a decimal")]


@pytest.mark.parametrize("day, total, expected", _test_data_outside_advent_season)
def test_discount_outside_advent_season (day: date, total: Decimal, expected: Decimal):
    # Act
    actual = calculate_discount(day, total)
    # Assert
    assert actual == expected

@pytest.mark.parametrize("day, total, expected", _test_data_inside_advent_season)
def test_discount_inside_advent_season (day: date, total: Decimal, expected: Decimal):
    # Act
    actual = calculate_discount(day, total)
    # Assert
    assert actual == expected

@pytest.mark.parametrize("day, total, expected", _test_saturdays_inside_advent_season)
def test_discount_saturdays_advent_season (day: date, total: Decimal, expected: Decimal):
    # Act
    actual = calculate_discount(day,total)
    # Assert
    assert actual == expected

@pytest.mark.parametrize("day, total ", _test_data_advent_season_robustness)
def test_robustness (day: date, total: Decimal):
    with pytest.raises(ValueError):
        calculate_discount(day, total)
