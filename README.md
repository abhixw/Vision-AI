# 🖼️ Vision AI — Image to Text using Groq

Vision AI is a simple web application that converts images into human-readable descriptions using Groq’s large language models and a modern Streamlit interface.

Users can paste any public image URL and instantly get an AI-generated caption explaining what the image contains.

---

## 🚀 Features

- Paste any public image URL
- AI analyzes the image and generates a natural language description
- Fast inference powered by Groq
- Clean and simple Streamlit web interface
- Works directly in the browser

---

## 🧠 How It Works

1. User pastes an image URL into the web app  
2. The URL is sent to Groq’s multimodal AI model  
3. The model understands the image and generates a caption  
4. The result is displayed in the Streamlit UI  

---

## 🛠 Tech Stack

- **Python**
- **Groq API**
- **Streamlit**
- **python-dotenv**

---

## 📂 Project Structure

image/
│
├── app.py # Streamlit UI
├── main.py # Groq AI logic
├── requirements.txt
└── .env # Groq API Key (not uploaded to GitHub)

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/vision-ai.git
cd vision-ai
2. Create and activate a virtual environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Add your Groq API key
Create a file named .env:

ini
Copy code
GROQ_API_KEY=your_groq_api_key_here
▶ Run the App
bash
Copy code
streamlit run app.py
Open in browser:

arduino
Copy code
http://localhost:8501
🧪 Example
Paste this in the app:

bash
Copy code
https://images.pexels.com/photos/2236713/pexels-photo-2236713.jpeg
The AI will generate a detailed caption describing the image.

📌 Future Improvements
Upload images instead of only URLs

History of previous captions

Download captions

Mobile-friendly UI

Deploy online

👤 Author
Abhinav Shrimali
Frontend Developer | AI Enthusiast

