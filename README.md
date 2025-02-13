# Data Science Tutor AI Assistant

An interactive Streamlit-based AI tutor for Data Science, powered by Google's Gemini model. Users can ask data science-related questions and receive detailed responses with examples. Includes a mentor support link for 1:1 Zoom calls. Secure API handling and user-friendly UI. 🚀  🔗 Live Demo | 📜 MIT License | 🤖 AI-Powered Assistance

The README is already in **Markdown format** (`.md`). However, if you're looking for a more structured version with **better readability**, here it is:

---

# 📚 Data Science Tutor Application

An interactive AI-powered tutor built with **Streamlit** and **Google's Gemini model** to provide detailed explanations of data science concepts. Users can ask data science-related questions and receive insightful responses with examples.

## 🚀 Features
- 🤖 **AI-powered tutoring** using Google's Gemini model
- 📚 **Detailed explanations** with real-world examples
- 🎨 **User-friendly UI** built with Streamlit
- 🔒 **Secure API handling** using environment variables or Streamlit Secrets
- 📞 **Mentor support** with a 1:1 Zoom call link for unresolved queries

## 📂 File Structure

📂 data-science-tutor-app/
│── 📂 .streamlit/              # Streamlit config directory
│   ├── secrets.toml            # Secure API key storage (for Streamlit Cloud)
│
│── 📂 src/                     # Source code folder
│   ├── app.py                  # Main Streamlit application
│   ├── tutor.py                # AI model configuration (keeps app.py clean)
│   ├── utils.py                # Helper functions
│
│── 📂 config/                   # Configuration files
│   ├── .env                    # Stores API keys (for local development)
│   ├── settings.py              # Global app settings
│
│── 📂 assets/                   # Static assets (if needed)
│   ├── logo.png                 # App logo
│   ├── styles.css               # Additional CSS styling
│
│── 📂 tests/                    # Unit and integration tests
│   ├── test_app.py              # Tests for Streamlit app
│   ├── test_tutor.py            # Tests for AI responses
│
│── 📂 docs/                     # Documentation
│   ├── README.md                # Project description
│   ├── requirements.txt         # Required Python packages
│   ├── setup_instructions.md    # Setup guide
│
│── .gitignore                   # Ignore unnecessary files (e.g., .env, secrets.toml)
│── requirements.txt              # List of dependencies
│── README.md                     # GitHub repository description

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/data-science-tutor-app.git
cd data-science-tutor-app
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up API Key (Secure Way)
- **For Local Development:** Create a `.env` file inside the `config/` folder:
  ```sh
  GOOGLE_API_KEY="your-secret-api-key"
  ```
- **For Streamlit Cloud:** Add your API key in `.streamlit/secrets.toml`:
  ```toml
  [google]
  api_key = "your-secret-api-key"
  ```

### 5️⃣ Run the Application
```sh
streamlit run src/app.py
```

## 🌍 Deployment
- 🚀 **Streamlit Cloud:** Upload the project and configure secrets.
- 🐳 **Docker:** Create a `Dockerfile` for easy containerization.
- ☁️ **Heroku/GCP/AWS:** Set up environment variables for deployment.

## 🤝 Contributing
Contributions are welcome! Feel free to **fork** the repo, create a **branch**, and submit a **pull request**.

## 📜 License
This project is licensed under the **MIT License**.

---

✉️ **Developed by Abhishek Kantharia** | 🌟 **Star this repo if you found it useful!** 🚀

---

### **Key Improvements in This Version:**
- **Emojis** 🎉 for better readability
- **Step-by-step guide** 🔢 for easy setup
- **Improved file structure formatting**
- **Highlighted commands** with **code blocks**  
