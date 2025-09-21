# AI Attorney - Virtual Legal Assistance

An AI-powered legal assistant application built with LangChain and Streamlit that helps users with legal document processing and legal consultation.

<!-- Updated: Force redeploy -->
## Features
- 📄 PDF document processing and analysis
- 💬 Interactive chat with AI attorney
- 🔍 Legal acts and regulations search
- 📰 Legal news updates
- 🏠 User-friendly homepage interface

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Bharathkondreddi/Virtual-AI-Attorney-for-Legal-Assistance.git
cd Virtual-AI-Attorney-for-Legal-Assistance
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Variables Setup
1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
2. Edit the `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_actual_openai_api_key_here
   ```
3. Get your OpenAI API key from: https://platform.openai.com/api-keys

### 4. Run the Application
```bash
streamlit run app.py
```

## Project Structure
```
├── app.py              # Main application file
├── chat.py             # Chat functionality
├── ActsSearch.py       # Legal acts search
├── about.py            # About page
├── home.py             # Homepage
├── news.py             # Legal news
├── codeexplain.py      # Code explanation features
├── htmlTemplates.py    # HTML templates
├── requirements.txt    # Python dependencies
├── images/             # Application images and logos
└── __pycache__/        # Python cache files
```

## Security Note
- Never commit your actual API keys to the repository
- Always use environment variables for sensitive information
- The `.env` file is ignored by Git for security purposes

## Deployment
This application can be deployed on platforms like:
- Streamlit Community Cloud
- Heroku
- AWS/Azure/GCP
- DigitalOcean

For deployment, make sure to set the `OPENAI_API_KEY` environment variable in your hosting platform's settings.

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License
This project is open source. Please check the license file for more details.

## Support
For support and questions, please open an issue in the GitHub repository.