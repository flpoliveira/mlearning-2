import pandas as pd


def test_0():
    answer = pd.read_csv("answer.csv")
    assert answer.shape == (26722, 2) 
    assert set(["index", "NO_OCDE_AREA_GERAL"]) == set(answer.columns)
