# Daily Status Report (DSR) – Streamlit Web App

This is a web-based **Daily Status Report (DSR)** tool built using [Streamlit](https://streamlit.io).  
It enables team members to submit, edit, and manage their daily work updates efficiently, with persistent storage for future reference.

## Features

- Form-based report submission
- Editable and filterable data table using `st.data_editor`
- Local CSV storage (can be upgraded to a database or Google Sheets)
- Minimal and clean UI for daily use by engineering teams

## Technologies Used

- Python 3.x
- Streamlit
- Pandas

## How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/LokeshAdivishnu/DailyStatusReport.git
   cd DailyStatusReport
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run dsr.py
   ```

4. Open your browser and visit: [http://localhost:8501](http://localhost:8501)

## Hosting on Streamlit Cloud

You can deploy this app for free using Streamlit Community Cloud:

1. Push this repository to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "Deploy an app" and link your GitHub repository
4. Set the main file as `app.py`
5. Click "Deploy" to make your app live

## License

This project is open-source and free for personal and educational use.

---

**Created by Lokesh Adivishnu**
