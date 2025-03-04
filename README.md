🌾 AI Assistant for Farmers 🚜
An AI-powered crop price prediction and real-time price fetching assistant for farmers, built with Flask, SerpAPI, and Machine Learning.

📌 Features
✅ Predicts crop prices using a trained ML model (Random Forest).
✅ Fetches real-time crop prices from Google Search (SerpAPI).
✅ State-wise crop price variations for better accuracy.
✅ Simple REST API with CORS support for frontend integration.
✅ Deployable on Render for cloud-based access.

🏗 Tech Stack
Backend: Flask, Scikit-Learn, Requests
Machine Learning: Random Forest Regression
Data Handling: Pandas, NumPy
Live Data Fetching: SerpAPI
Deployment: Render
🚀 Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/ai-assistant-farmers.git
cd ai-assistant-farmers
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Set Up Environment Variables
Create a .env file or set manually:
export SERPAPI_KEY="your_actual_serpapi_key"
(For Windows Command Prompt)
set SERPAPI_KEY=your_actual_serpapi_key
4️⃣ Run the Flask App
python app.py
📌 Check API Status
http
Copy
Edit
GET /
Response:
{
    "message": "Crop Price Prediction API is running!"
}
📌 Get Predicted & Live Crop Price
GET /predict_price?crop_name=Rice
Response Example:
{
    "crop_name": "Rice",
    "predicted_price": 32.45,
    "predicted_price_integer": 32,
    "live_price": 31
}
🌍 Deploying on Render
1️⃣ Create requirements.txt
Make sure it contains:
Flask
flask-cors
numpy
pandas
requests
scikit-learn
waitress

2️⃣ Push to GitHub
git add .
git commit -m "Initial commit"
git push origin main

3️⃣ Deploy on Render
Go to Render → New Web Service
Connect GitHub repo
Set Start Command: python app.py
Add Environment Variable (SERPAPI_KEY)
Deploy & Test API! 🎉
📩 Contributing
Fork the repo
Create a new branch (git checkout -b feature-xyz)
Commit changes (git commit -m "Added new feature")
Push to branch (git push origin feature-xyz)
Open a Pull Request
🎯 Future Enhancements
🔹 Weather-based crop recommendations
🔹 AI chatbot for farmer queries
🔹 Crop disease detection using ML

📜 License
🔓 MIT License - Free to use & modify!

⭐ Show Support
🌟 Star this repo if you like it!
