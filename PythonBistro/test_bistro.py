from utils import calculate_subtotal, calculate_gst, calculate_total

def test_single_item():
    assert calculate_subtotal({1: 2}) == 240

def test_multiple_items():
    assert calculate_subtotal({1: 2, 3: 1, 9: 2}) == 430

def test_gst():
    assert calculate_gst(1000) == 50

def test_final_total():
    assert calculate_total(1000) == 1050

def test_empty_order():
    assert calculate_subtotal({}) == 0

def test_complete_bill_calculation():
    order = {2: 1, 4: 2, 8: 2}
    subtotal = calculate_subtotal(order)
    assert subtotal == 390
    assert calculate_gst(subtotal) == 19.5
    assert calculate_total(subtotal) == 409.5

def run_tests():
    test_single_item()
    test_multiple_items()
    test_gst()
    test_final_total()
    test_empty_order()
    test_complete_bill_calculation()
    print("ALL TESTS PASSED!")

if __name__ == "__main__":
    run_tests()
