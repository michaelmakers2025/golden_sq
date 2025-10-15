from lib.high_value import HighValue

def test_first_value():
    hv = HighValue(10, 20)

    assert hv.value_second == 20
    assert hv.value_first == 10

def test_first_value_higher():
    hv = HighValue(30, 10)

    assert hv.get_highest() == "First value is higher"

def test_second_value_higher():
    hv = HighValue(10, 30)

    assert hv.get_highest() == "Second value is higher"

def test_values_are_equal():
    hv = HighValue(10, 10)

    assert hv.get_highest() == "Values are equal"

def test_add_increase_first_by_10():
    hv = HighValue(30, 10)
    hv.add(10, "first")

    assert hv.value_first  == 40

def test_add_increase_second_by_30():
    hv = HighValue(30, 10)
    hv.add(30, "second")

    assert hv.value_second == 40
