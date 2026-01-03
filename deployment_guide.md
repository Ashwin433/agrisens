# Deployment Guide for AgriSens

This guide will help you host your Django project on **Render** (a popular platform with a free tier).

## Prerequisites

1.  **GitHub Account**: Your code must be pushed to a GitHub repository.
2.  **Render Account**: Sign up at [render.com](https://render.com).

## Steps to Deploy

### 1. Push to GitHub
If you haven't already, push your code to a new GitHub repository.
```bash
git add .
git commit -m "Prepare for deployment"
git push origin main
```

### 2. Create Database on Render
1.  Go to your Render Dashboard.
2.  Click **New +** -> **PostgreSQL**.
3.  Name it `agrisens-db`.
4.  Choose the **Free** plan.
5.  Click **Create Database**.
6.  Wait for it to be created. Note the "Internal Database URL" (you shouldn't need to copy it manually if you link it, but keep it in mind).

### 3. Create Web Service on Render
1.  Go to Dashboard, click **New +** -> **Web Service**.
2.  Connect your GitHub repository.
3.  Give it a unique name (e.g., `agrisens-app`).
4.  **Region**: Choose the same region as your database.
5.  **Branch**: `main` (or master).
6.  **Root Directory**: Leave empty (since `manage.py` is in root).
7.  **Runtime**: `Python 3`.
8.  **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
    *   *Note: This installs dependencies and prepares static files.*
9.  **Start Command**: `gunicorn agrisens.wsgi`
10. **Instance Type**: Free.

### 4. Configure Environment Variables
Scroll down to the **Environment Variables** section and add:

| Key | Value |
| :--- | :--- |
| `PYTHON_VERSION` | `3.9.0` (or your local version) |
| `SECRET_KEY` | (Generate a long random string using a tool or python) |
| `DEBUG` | `False` |
| `DATABASE_URL` | (See step below) |

**Linking the Database:**
Instead of pasting the URL manually:
1.  Click **Advanced** or find settings to adding a database.
2.  Actually, on the "Active Environment" or "Environment" section, you might see an option to link a database.
3.  IF NOT, go to your created Database page, copy the **Internal Database URL**.
4.  Add it as an environment variable named `DATABASE_URL` in your Web Service.

### 5. Deploy
1.  Click **Create Web Service**.
2.  Render will start building your app. Watch the logs.
3.  It might take a few minutes.
4.  Once live, it will give you a URL (e.g., `agrisens-app.onrender.com`).

### 6. Run Migrations
Since we are using a new database, we need to create tables.
1.  In the Render Dashboard for your Web Service, go to the **Shell** tab (available on paid plans usually, but for free tier you might need to add it to build command or use a job).
    *   *Workaround for Free Tier*:
        Change your **Build Command** temporarily to:
        `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
        Then trigger a manual deploy.
        *After it succeeds*, change it back to remove the migrate command (to avoid running it every time if you want faster builds, though it's usually safe to keep).

## Troubleshooting
-   **Static Files**: If images/CSS are missing, check `whitenoise` configuration in `settings.py`.
-   **Database Errors**: Ensure `DATABASE_URL` is correct.

Good luck!
