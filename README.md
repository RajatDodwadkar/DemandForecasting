# 📊 DemandForecasting

A Django-based demand forecasting platform using MySQL, built to predict demand trends from historical data.

> 🐍 Python 3.10.6 | 🛠 Linux Environment | 💾 MySQL DB

---

## 🚀 Quick Setup

1. **Clone & Navigate**
```bash
git clone https://github.com/yourusername/DemandForecasting.git
cd DemandForecasting
```

2. **(Optional) Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install Requirements**
```bash
pip install -r requirements.txt
```

4. **Add `.env` in project root**
```env
SECRET_KEY='your_django_secret_key'
DB_NAME='your_database_name'
DB_USER='your_database_user'
DB_PASSWORD='your_database_password'
DB_HOST='your_database_host'
```

5. **Run Migrations**
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

6. **Create Admin User**
```bash
python3 manage.py createsuperuser
```

7. **Start the Server**
```bash
python3 manage.py runserver
```

---

## 📁 Highlights

- 🔍 Forecast demand using historical datasets
- 🧠 Scalable structure for ML model integration
- 🖥️ Admin dashboard for data operations
- 🛡️ Secure with environment-based configuration

---

## ⚙️ Tech Stack

- **Backend:** Django
- **Database:** MySQL
- **Tools:** Python, dotenv, virtualenv

---

## 📄 License

Licensed under the [MIT License](LICENSE).
