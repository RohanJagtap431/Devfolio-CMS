# Devfolio CMS 🚀

A modern, responsive developer portfolio website built with **Django**. It includes a custom admin CMS that allows you to manage portfolio content dynamically without editing code.

## 🌐 Live Demo

**Website:** https://devfolio-cms.onrender.com/

**Admin Panel:** https://devfolio-cms.onrender.com/admin/

## ✨ Features

- Dynamic Developer Portfolio
- Custom Django Admin CMS
- Profile and About Section Management
- Skills Management
- Project Management
- Individual Project Details Pages
- Project Features and Challenges
- Project Image Gallery
- Experience Timeline
- Certificates and Achievements
- Contact Form with Admin Message Management
- Responsive Dark Theme
- SEO Meta Tags
- XML Sitemap
- Robots.txt
- Cloudinary Media Storage
- PostgreSQL Database

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend Programming |
| Django | Web Framework |
| PostgreSQL | Database |
| HTML5 | Structure |
| CSS3 | Styling |
| JavaScript | Interactivity |
| Cloudinary | Media Storage |
| WhiteNoise | Static Files |
| Gunicorn | WSGI Server |
| Render | Deployment |
| Git & GitHub | Version Control |

## 📁 Project Structure

```text
Devfolio-CMS/
│
├── accounts/
├── certificates/
├── config/
├── contact/
├── core/
├── experience/
├── portfolio/
├── projects/
├── skills/
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── templates/
│   ├── core/
│   └── projects/
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/RohanJagtap431/Devfolio-CMS.git
```

### 2. Open Project Directory

```bash
cd Devfolio-CMS
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root directory.

```env
SECRET_KEY=your-secret-key
DEBUG=True

ALLOWED_HOSTS=127.0.0.1,localhost
CSRF_TRUSTED_ORIGINS=

DATABASE_URL=your-postgresql-database-url

CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

Replace the placeholder values with your own credentials.

**Never upload your `.env` file or secret credentials to GitHub.**

### 7. Run Database Migrations

```bash
python manage.py migrate
```

### 8. Create Admin Account

```bash
python manage.py createsuperuser
```

### 9. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 10. Run Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

## 🚀 Deployment

This project is deployed using Render.

**Build Command:**

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

**Start Command:**

```bash
gunicorn config.wsgi:application
```

Configure the required environment variables in the Render dashboard before deployment.

## 🔐 Security

- Environment variables for sensitive credentials.
- Django CSRF protection.
- Secure production cookies.
- Configurable allowed hosts.
- `.env` excluded through `.gitignore`.

## 👨‍💻 Developer

**Rohan Jagtap**

Python / Django Backend Developer

- GitHub: [@RohanJagtap431](https://github.com/RohanJagtap431)
- Project Repository: [Devfolio-CMS](https://github.com/RohanJagtap431/Devfolio-CMS)

---

⭐ If you find this project useful, consider giving it a star!

**Built with Python and Django.**
