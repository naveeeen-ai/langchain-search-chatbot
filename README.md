# LangChain Search Chatbot

A powerful Streamlit-based chatbot that combines OpenAI's GPT models with real-time web search capabilities using DuckDuckGo. This application allows users to ask questions and get up-to-date answers by leveraging both AI language models and current web information.

## ✨ Features

- **AI-Powered Responses**: Uses OpenAI's GPT-4o-mini model for intelligent question answering
- **Web Search Integration**: Incorporates real-time web search using DuckDuckGo for current information
- **Dual Mode Operation**: 
  - Web search enabled: Gets current, up-to-date information
  - Basic mode: Relies solely on the AI model's training data
- **User-Friendly Interface**: Clean Streamlit web interface
- **Error Handling**: Robust error handling for search and API failures

## 🛠️ Technologies Used

- **LangChain**: Framework for developing applications with language models
- **OpenAI GPT-4o-mini**: Advanced language model for generating responses
- **DuckDuckGo Search**: Privacy-focused search engine for web results
- **Streamlit**: Web application framework for the user interface
- **Python 3.12+**: Programming language

## 📋 Prerequisites

- Python 3.12 or higher
- OpenAI API key
- Internet connection for web search functionality

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/naveeeen-ai/langchain-search-chatbot.git
   cd langchain-search-chatbot
   ```

2. **Install dependencies:**
   uv (recommended):
   ```bash
   pip install uv
   uv sync
   ```

3. **Set up environment variables:**
   Create a `.env` file in the project root and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 💻 Usage

1. **Run the Streamlit application:**
   ```bash
   streamlit run chatbot.py
   ```

2. **Open your browser** and navigate to the provided local URL (typically `http://localhost:8501`)

3. **Ask questions:**
   - Enter your question in the text input field
   - Choose whether to enable web search (recommended for current events/information)
   - Click "Generate Answer" to get your response

## 📁 Project Structure

```
langchain-search-chatbot/
├── chatbot.py          # Main Streamlit application
├── main.py            # Basic Python entry point
├── pyproject.toml     # Project configuration and dependencies
├── .env               # Environment variables (create this)
├── .gitignore         # Git ignore rules
└── README.md          # Project documentation
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key for GPT model access | Yes |

### Model Configuration

The chatbot uses GPT-4o-mini by default with a temperature of 0.7. You can modify these settings in `chatbot.py`:

```python
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
```

## 🎯 Use Cases

- **Research**: Get current information on any topic
- **News Updates**: Ask about recent events and developments
- **General Questions**: Leverage AI knowledge for various inquiries
- **Fact Checking**: Combine AI responses with web search for verification

## 📦 Dependencies

The project uses the following main dependencies (see `pyproject.toml` for complete list):

- `streamlit>=1.46.1` - Web application framework
- `langchain>=0.3.26` - LangChain framework
- `langchain-community>=0.3.26` - Community integrations
- `langchain-openai` - OpenAI integration
- `duckduckgo-search>=8.0.4` - Web search functionality

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## ⚠️ Important Notes

- **API Costs**: This application uses OpenAI's API, which may incur costs based on usage
- **Rate Limits**: Be aware of OpenAI API rate limits
- **Privacy**: DuckDuckGo search is used for privacy-focused web searches
- **Environment**: Keep your `.env` file secure and never commit it to version control

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your OpenAI API key is correctly set in the `.env` file
2. **Import Errors**: Make sure all dependencies are installed using `pip install -r requirements.txt`
3. **Search Failures**: Check your internet connection if web search is not working

### Getting Help

If you encounter issues:
1. Check the console output for error messages
2. Verify your OpenAI API key is valid and has sufficient credits
3. Ensure all dependencies are properly installed


