from compound import compound

def test_compound():
    fv = compound(present_value=100, interest_rate=0.10, time=3)
    assert fv == 133.10000000000005
