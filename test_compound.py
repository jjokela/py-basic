import pytest

from compound import compound, compound_yearly_value_with_interest


def test_compound():
    fv = compound(present_value=100, interest_rate=0.10, time=3)
    assert fv == 133.10000000000005


def test_compound_yearly_value_with_interest():
    result = compound_yearly_value_with_interest(present_value=100, interest_rate=0.10, time=3)
    print(result)
    assert result[0][0] == pytest.approx(100.0)
    assert result[1][0] == pytest.approx(110.0)
    assert result[2][0] == pytest.approx(121.0)

    assert result[0][1] == pytest.approx(0.0)
    assert result[1][1] == pytest.approx(10.0)
    assert result[2][1] == pytest.approx(11.0)
