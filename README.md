# Ollama_websearch

---

# Internet Search Assistant with Llama 3.2

This project is a simple web application that combines the power of the Llama 3.2 language model with real-time web search capabilities to provide concise and accurate answers to user queries. It leverages Streamlit for the user interface and integrates DuckDuckGo for web search results.

## Features

- **AI-Powered Responses**: Utilizes the Llama 3.2 model to generate human-like responses.
- **Web Search Integration**: Fetches relevant context using DuckDuckGo's API.
- **Streamlit Interface**: Easy-to-use web-based UI for seamless interaction.

## Prerequisites

- Python 3.8 or higher
- A running instance of the Llama 3.2 model
- Required Python libraries (see [Installation](#installation))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that the Llama 3.2 model is running locally. Update the `base_url` in the script if necessary.

## Usage

1. Start the application:
   ```bash
   streamlit run Websearch_LLM.py
   ```

2. Open the app in your browser at `http://localhost:8501`.

3. Enter a question in the input field and click the "Search and Answer" button to get a response based on web search results.

## File Structure

- `Websearch_LLM.py`: The main script containing the application logic.
- `requirements.txt`: A list of Python dependencies for the project.

## Key Components

- **Llama 3.2 Integration**: Configured to use the local Llama 3.2 model with specified parameters for generating responses.
- **DuckDuckGo API Wrapper**: Fetches up to 5 search results for user queries.
- **Streamlit Interface**: Provides a simple text input for questions and displays AI-generated answers.

## Dependencies

The project relies on the following Python libraries:
- `streamlit`
- `langchain-community`
- `langchain-core`

## Example

1. Enter a query, e.g., "What is the capital of France?"
2. The app performs a web search and provides a concise answer like "The capital of France is Paris."

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.
