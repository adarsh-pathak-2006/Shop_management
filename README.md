# Utsav Dukan API

A modern, robust inventory and sales management API built with Django Rest Framework. Designed to track product stock in real-time, record customer sales, and prevent overselling using automated database integrations and Redis caching for optimal performance.

## 🚀 Features

* **Inventory Management**: Create, read, update, and delete product categories and individual products.
* **Real-time Stock Updates**: Automatically deducts product stock when a sale is recorded.
* **Oversell Protection**: Implements strict data validation to block any transactions if requested quantity exceeds available stock.
* **High Performance**: Endpoints are aggressively cached using Redis to minimize database loads.
* **Production Ready**: Fully configured for deployment on Render with WhiteNoise static file serving and PostgreSQL integration.

## 🛠 Tech Stack

* **Framework:** Django & Django Rest Framework (DRF)
* **Database:** SQLite (Local) / PostgreSQL (Production)
* **Caching:** Redis (`django-redis`)
* **Deployment:** Render (`gunicorn`, `whitenoise`, `dj-database-url`)

## 💻 Local Setup

Follow these steps to run the project locally on your machine.

### Prerequisites
* Python 3.10+
* Redis Server running on `127.0.0.1:6379`

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd utsav
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   The project uses `python-dotenv`. A `.env` file is required.
   Copy the example file and update it if necessary:
   ```bash
   cp .env.example .env
   ```
   *Note: Local development defaults to SQLite, so you can leave `DATABASE_URL` blank in your `.env` file.*

5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```

## 🌍 Deployment (Render + Neon DB + External Redis)

This project is fully configured for deployment on Render.com, utilizing **Neon DB** for serverless PostgreSQL and a third-party Redis provider (like **Upstash** or **Redis Cloud**).

1. Create a new **Web Service** on Render and connect your GitHub repository.
2. Under the service settings, configure the following:
   * **Build Command:** `./build.sh`
   * **Start Command:** `gunicorn utsav.wsgi:application`
3. Add the following **Environment Variables** to your Web Service:
   * `SECRET_KEY`: Set to a long, random string.
   * `DEBUG`: `False`
   * `ALLOWED_HOSTS`: `<your-app-name>.onrender.com`
   * `DATABASE_URL`: Your **Neon DB** connection string (e.g., `postgres://user:pass@ep-rest-of-url.neon.tech/dbname?sslmode=require`).
   * `CACHE_URL`: Your third-party Redis connection string (e.g., from Upstash).
5. Click **Deploy**. Render will automatically install dependencies, collect static files, and migrate the remote database.

## 📡 API Endpoints

### Inventory
* `GET /inventory/category/` - List all categories
* `POST /inventory/category/` - Create a new category
* `GET /inventory/product/` - List all products
* `POST /inventory/product/` - Create a new product

### Customer / Sales
* `GET /customer/product-sold/` - List all individual sold product records
* `POST /customer/product-sold/` - Record a product sale (automatically deducts inventory)
* `GET /customer/sale/` - List all master sale receipts
* `POST /customer/sale/` - Create a master sale receipt

---
*Developed for Utsav Dukan*
