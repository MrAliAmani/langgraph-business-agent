import pytest
from main import graph

def test_negative_profit_and_high_cac():
    data = {
        "today":     {"revenue":  900, "cost": 1100, "customers": 20},
        "yesterday": {"revenue": 1000, "cost":  800, "customers": 20}
    }
    result = graph.invoke(data)

    # Expect loss alert
    assert "Reduce costs if profit is negative." in result["alerts"]
    # Expect CAC‐increase alert (>20% increase)
    assert any("CAC increased significantly" in a for a in result["alerts"])

if __name__ == "__main__":
    pytest.main()
