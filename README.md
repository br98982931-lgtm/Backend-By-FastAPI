# 📝 Registration System using Streamlit & FastAPI

A simple full-stack Registration System built using **Streamlit** as the frontend and **FastAPI** as the backend.

Users can enter their registration details through a web form. The Streamlit frontend sends the data to the FastAPI backend using a POST API, and the backend stores the registration data in a JSON file.

## 🚀 Live Demo

### 🌐 Streamlit Frontend
👉 https://backend-by-fastapi-2.onrender.com

Use this link to open the registration form and submit user details.

### ⚡ FastAPI Backend
👉 https://backend-by-fastapi-1.onrender.com

### ⚡ Swagger UI
👉 https://backend-by-fastapi-1.onrender.com/docs

FastAPI provides the backend REST API and interactive Swagger documentation.

## 🏗️ Project Architecture

```text
                 User
                   │
                   ▼
        ┌─────────────────────┐
        │ Streamlit Frontend  │
        │ Registration Form   │
        └──────────┬──────────┘
                   │
                   │ POST /register
                   ▼
        ┌─────────────────────┐
        │   FastAPI Backend   │
        │     REST API        │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │  registrations.json │
        │      Database       │
        └─────────────────────┘
