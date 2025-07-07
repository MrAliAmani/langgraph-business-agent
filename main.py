from langgraph.graph import StateGraph

# 1) Input node: just passes through incoming JSON/dict
def input_node(data: dict) -> dict:
    return data

# 2) Processing node: compute profit, percent-changes, CAC changes
def processing_node(data: dict) -> dict:
    today = data["today"]
    yesterday = data["yesterday"]

    # Basic metrics
    profit = today["revenue"] - today["cost"]
    profit_status = "Profit" if profit >= 0 else "Loss"

    revenue_change = ((today["revenue"] - yesterday["revenue"]) 
                      / yesterday["revenue"]) * 100
    cost_change = ((today["cost"] - yesterday["cost"]) 
                   / yesterday["cost"]) * 100

    cac_today = today["cost"] / today["customers"]
    cac_yesterday = yesterday["cost"] / yesterday["customers"]
    cac_change = ((cac_today - cac_yesterday) / cac_yesterday) * 100

    return {
        "profit": profit,
        "profit_status": profit_status,
        "revenue_change_percent": revenue_change,
        "cost_change_percent": cost_change,
        "cac_change_percent": cac_change
    }

# 3) Recommendation node: produce actionable advice
def recommendation_node(metrics: dict) -> dict:
    alerts = []

    if metrics["profit"] < 0:
        alerts.append("Reduce costs if profit is negative.")
    if metrics["cac_change_percent"] > 20:
        alerts.append("Review marketing campaigns; CAC increased significantly.")
    if metrics["revenue_change_percent"] > 0:
        alerts.append("Consider increasing advertising budget; sales are growing.")

    return {
        "profit_status": metrics["profit_status"],
        "alerts": alerts
    }

# 4) Build and compile the LangGraph
builder = StateGraph()
builder.add_node("input", input_node)
builder.add_node("process", processing_node)
builder.add_node("recommend", recommendation_node)

builder.set_entry_point("input")
builder.add_edge("input", "process")
builder.add_edge("process", "recommend")

# Export a ready-to-run graph object
graph = builder.compile()

if __name__ == "__main__":
    # Example invocation
    sample = {
        "today":       {"revenue": 1200, "cost": 800,  "customers": 40},
        "yesterday":   {"revenue": 1000, "cost": 700,  "customers": 35}
    }
    output = graph.invoke(sample)
    print(output)
