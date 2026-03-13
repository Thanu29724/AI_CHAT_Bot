# 🤖 AI Chatbot using LangChain + Groq

This project is a simple AI chatbot built using **LangChain**, **Groq LLM**, and **Streamlit**.
It allows users to interact with a powerful language model through a web interface.

The application processes user questions and generates intelligent responses using the Groq-hosted Llama model.

---

## 🚀 Features

* Interactive AI chatbot interface
* Built with LangChain framework
* Uses Groq LLM for fast responses
* Streamlit web interface
* LangSmith tracing support for monitoring LLM runs
* Easy deployment on Streamlit Cloud

---

## 🛠️ Technologies Used

* Python
* LangChain
* Groq API
* Streamlit
* LangSmith
* Llama 3.1 Model

---

## 📂 Project Structure

```
ai_chat_bot/
│
├── app.py
├── chat.ipynb
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/ai_chat_bot.git
cd ai_chat_bot
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file and add your API key:

```
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Application

```
streamlit run app.py
```

The application will start at:

```
http://localhost:8501
```

---

## 🌐 Deployment

This project can be deployed using **Streamlit Community Cloud**.

Steps:

1. Upload project to GitHub
2. Connect repository to Streamlit Cloud
3. Add the Groq API key in Streamlit Secrets
4. Deploy the application

---

## 📌 Example

User Input:

```
What is Artificial Intelligence?
```

AI Response:

```
Artificial Intelligence is the simulation of human intelligence in machines that can learn, reason, and solve problems.
```

---

## 📈 Future Improvements

* Chat history support
* Document question answering (RAG)
* Voice input support
* Multi-model selection

---

## 👨‍💻 Author

Thanush M N

Electronics & Communication Engineering Student

thanushmn29@gmail.com

---

⭐ If you like this project, consider giving it a star on GitHub!
