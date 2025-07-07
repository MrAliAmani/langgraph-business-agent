from main import graph

def run_tests():
    """Runs all validation tests for the agent."""
    print("--- Running Test 1: Negative Profit and High CAC ---")
    test_negative_profit_and_high_cac()
    print("Test 1 Passed.")

    print("\n--- Running Test 2: Positive Growth Scenario ---")
    test_positive_growth_scenario()
    print("Test 2 Passed.")

    print("\nAll tests passed successfully!")

def test_negative_profit_and_high_cac():
    """Tests the scenario with negative profit and high CAC increase."""
    data = {
        "today":     {"revenue":  900, "cost": 1100, "customers": 20},
        "yesterday": {"revenue": 1000, "cost":  800, "customers": 20}
    }
    result = graph.invoke(data)
    recommendations = result["recommendations"]

    # Validate profit status and alerts
    assert recommendations["profit_status"] == "Loss"
    assert "Alert: Profit is negative." in recommendations["alerts"]
    assert any("Warning: CAC increased by" in a for a in recommendations["alerts"])

    # Validate decision-making recommendations
    assert "Action: Reduce costs to improve profitability." in recommendations["decision_making_recommendations"]
    assert "Action: Review marketing campaigns for efficiency." in recommendations["decision_making_recommendations"]

def test_positive_growth_scenario():
    """Tests the scenario with positive profit and revenue growth."""
    data = {
        "today":     {"revenue": 1200, "cost": 800,  "customers": 40},
        "yesterday": {"revenue": 1000, "cost": 900,  "customers": 35}
    }
    result = graph.invoke(data)
    recommendations = result["recommendations"]

    # Validate profit status and alerts
    assert recommendations["profit_status"] == "Profit"
    assert any("Info: Sales are growing" in a for a in recommendations["alerts"])
    assert len(recommendations["alerts"]) == 1 # Ensure no other warnings are present

    # Validate decision-making recommendations
    assert "Action: Consider increasing advertising budget to fuel growth." in recommendations["decision_making_recommendations"]

if __name__ == "__main__":
    run_tests()
