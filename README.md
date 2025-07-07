# Simple AI Business Analyst Agent

This project is a simple AI agent built with LangGraph that analyzes basic business data (daily sales and costs) and generates a summary report with actionable recommendations.

## Features

- **Profit/Loss Calculation**: Calculates the daily profit or loss based on revenue and cost.
- **Trend Analysis**: Compares today's sales and costs with the previous day to identify trends.
- **CAC Monitoring**: Calculates the Customer Acquisition Cost (CAC) and warns if it increases by more than 20%.
- **Actionable Recommendations**: Provides clear, actionable advice based on the data analysis, such as suggesting cost reductions or marketing campaign reviews.

## Technologies Used

- Python
- LangGraph
- LangChain
- Pytest
- LangGraph CLI

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MrAliAmani/langgraph-business-agent.git
   cd Studio
   ```
2. **Create and activate a virtual environment:**

   ```bash
   # For Windows
   python -m venv venv
   .\venv\Scripts\activate

   # For macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Agent Directly

You can run the agent directly from the command line to see a sample output.

```bash
python main.py
```

This will run the agent with the sample data defined in `main.py` and print the resulting recommendations.

### Running Tests

The project includes a test suite to validate the agent's logic.

```bash
python test_agent.py
```

This will execute the tests and print a success message if all tests pass.

## Testing with LangGraph Studio

LangGraph Studio provides a visual interface to run, debug, and interact with your agent.

### Prerequisites

- **Docker**: You must have Docker Desktop installed and running. You can download it from [here](https://www.docker.com/products/docker-desktop/).

### Launching the Studio

1. **Navigate to the project directory** in your terminal.
2. **Run the `langgraph up` command:**

   ```bash
   langgraph up
   ```
   This command will:

   - Start the necessary Docker containers.
   - Find the `graph` object in `main.py` (based on your `langgraph.json` file).
   - Launch the LangGraph Studio server.
   - Automatically open LangGraph Studio in your default web browser.
3. **Interact with the Agent in Studio:**

   - Once Studio is open, you will see a visual representation of your agent's graph.
   - You can provide your own input data (in JSON format) in the input panel.
   - Click "Run" to execute the agent and see the data flow through the nodes in real-time.
