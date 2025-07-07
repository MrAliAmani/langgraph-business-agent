from langgraph.graph import StateGraph
from typing import List
from typing_extensions import TypedDict

# 1) Define the state for our graph
class AgentState(TypedDict):
    today: dict
    yesterday: dict
    profit: float
    profit_status: str
    revenue_change_percent: float
    cost_change_percent: float
    cac_change_percent: float
    recommendations: dict

# 2) Processing node: compute profit, percent-changes, CAC changes
def processing_node(state: AgentState) -> dict:
    today = state["today"]
    yesterday = state["yesterday"]

    # Basic metrics
    profit = today["revenue"] - today["cost"]
    profit_status = "Profit" if profit >= 0 else "Loss"

    # Handle division by zero for revenue/cost change
    revenue_change = (((today["revenue"] - yesterday["revenue"]) / yesterday["revenue"]) * 100 
                      if yesterday["revenue"] != 0 else 0)
    cost_change = (((today["cost"] - yesterday["cost"]) / yesterday["cost"]) * 100 
                   if yesterday["cost"] != 0 else 0)

    # Handle division by zero for CAC
    cac_today = today["cost"] / today["customers"] if today["customers"] > 0 else 0
    cac_yesterday = yesterday["cost"] / yesterday["customers"] if yesterday["customers"] > 0 else 0
    cac_change = (((cac_today - cac_yesterday) / cac_yesterday) * 100 
                  if cac_yesterday != 0 else 0)

    return {
        "profit": profit,
        "profit_status": profit_status,
        "revenue_change_percent": revenue_change,
        "cost_change_percent": cost_change,
        "cac_change_percent": cac_change,
    }

# 3) Recommendation node: produce actionable advice
def recommendation_node(state: AgentState) -> dict:
    alerts = []
    recommendations = []

    if state["profit"] < 0:
        alerts.append("Alert: Profit is negative.")
        recommendations.append("Action: Reduce costs to improve profitability.")

    if state["cac_change_percent"] > 20:
        alerts.append(f"Warning: CAC increased by {state['cac_change_percent']:.2f}%.")
        recommendations.append("Action: Review marketing campaigns for efficiency.")

    if state["revenue_change_percent"] > 10: # If sales are growing well
        alerts.append(f"Info: Sales are growing ({state['revenue_change_percent']:.2f}% increase).")
        recommendations.append("Action: Consider increasing advertising budget to fuel growth.")

    return {
        "recommendations": {
            "profit_status": state["profit_status"],
            "alerts": alerts,
            "decision_making_recommendations": recommendations,
        }
    }

# 4) Build and compile the LangGraph
builder = StateGraph(AgentState)

builder.add_node("process", processing_node)
builder.add_node("recommend", recommendation_node)

builder.set_entry_point("process")
builder.add_edge("process", "recommend")
builder.set_finish_point("recommend")

# Export a ready-to-run graph object for LangGraph Studio
graph = builder.compile()

if __name__ == "__main__":
    # Example invocation
    sample_input = {
        "today":       {"revenue": 1200, "cost": 800,  "customers": 40},
        "yesterday":   {"revenue": 1000, "cost": 700,  "customers": 35}
    }
    # The input to invoke should match the initial state keys required by the entry point
    output = graph.invoke(sample_input)
    print(output.get('recommendations'))
