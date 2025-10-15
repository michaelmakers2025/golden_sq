from lib.counter import Counter

def test_counter_is_zero():
    counter = Counter()
    assert counter.count == 0

def test_add_updates_count_to_equal_5():
    counter = Counter()
    counter.add(5)
    assert counter.count == 5

def test_add_updates_count_to_equal_7():
    counter = Counter()
    counter.add(7)
    assert counter.count == 7

def test_add_changes_count_report():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."

