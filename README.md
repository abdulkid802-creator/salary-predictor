# 💼 Data Science Salary Predictor

A machine learning web app that estimates data science salaries based on role, experience, location, and work setup.

Built with Python, scikit-learn, and Streamlit.

---

## 🚀 Demo

Enter your job title, experience level, company location and more — get an instant salary estimate in USD.

---

## 📁 Project Structure

```
salary-predictor/
├── app.py              # Streamlit web app
├── model.pkl           # Trained ML model
├── job_map.json        # Job title encodings
├── res_map.json        # Employee residence encodings
├── loc_map.json        # Company location encodings
├── requirements.txt    # Python dependencies
├── data/
│   └── ds_salaries.csv # Dataset
└── notebooks/
    └── 01_eda.ipynb    # Exploratory data analysis & model training
```

---

## 🧠 How It Works

1. User selects inputs: job title, experience level, employment type, remote ratio, company size, location, and work year
2. Inputs are encoded using pre-built mapping files
3. A trained scikit-learn model predicts the salary in USD

---

## ⚙️ Setup & Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/abdulkid802-creator/salary-predictor.git
cd salary-predictor
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the app**
```bash
streamlit run app.py
```

---

## 📊 Dataset

The model was trained on the [Data Science Job Salaries dataset](https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries), which includes salary data from 2020–2023 across various roles, countries, and company sizes.

---

## 🔧 Model

- Algorithm: scikit-learn (see `notebooks/01_eda.ipynb` for details)
- Features: work year, experience level, employment type, job title, employee residence, remote ratio, company location, company size
- Target: salary in USD

---

## 📬 Contact

Built by Abdul — [@abdulkid802-creator](https://github.com/abdulkid802-creator)
