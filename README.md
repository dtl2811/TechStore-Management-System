# TechStore Management System

A full-stack web application for managing the core operations of a technology retail store. The project uses Django and MySQL for the backend, with React, Vite, and TypeScript for the frontend.

**Project status:** Under development

## Overview

TechStore Management System aims to organize product information, inventory, shopping carts, orders, suppliers, and promotions in one application.

The project separates the backend and frontend to support maintainability and future development. Its database models are organized around the main entities and relationships of an online technology store.

## Tech Stack

### Backend

* Python
* Django
* MySQL

### Frontend

* React
* Vite
* TypeScript

### Development Tools

* Git
* npm
* Python virtual environment (`venv`)

## Features and Modules

The current project structure includes models and database tables for the following areas:

* **Accounts:** Users, roles, customers, addresses, and reviews
* **Products:** Categories, brands, products, product images, and product variants
* **Shopping Cart:** Carts, cart items, wishlists, and wishlist items
* **Orders:** Orders, order items, payments, and shipments
* **Inventory:** Inventory records and inventory transactions
* **Suppliers:** Suppliers, purchase orders, and purchase order items
* **Promotions:** Promotions and promotion-product relationships

The application is still under development. The presence of a model or database table does not necessarily mean its complete user-facing functionality is available.

## Project Structure

```text
TechStore-Management-System/
├── backend/
│   ├── accounts/
│   ├── cart/
│   ├── orders/
│   ├── products/
│   ├── promotions/
│   ├── suppliers/
│   ├── techstore/
│   ├── requirements.txt
│   └── manage.py
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

Install the following tools:

* Git
* Python
* Node.js and npm
* MySQL Server

### 1. Clone the Repository

```bash
git clone https://github.com/dtl2811/TechStore-Management-System.git
cd TechStore-Management-System
```

### 2. Set Up the Backend

From the project root, create and activate a virtual environment.

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
cd backend
pip install -r requirements.txt
```

### 3. Configure the Database

Create a MySQL database named `techstore`.

Configure the database connection using these environment variables in PowerShell:

```powershell
$env:DB_USER = "root"
$env:DB_PASSWORD = Read-Host "Enter your MySQL password"
$env:DB_HOST = "127.0.0.1"
$env:DB_PORT = "3306"
```

Enter your own MySQL password when prompted. Do not commit database passwords or other sensitive credentials to Git.

**Note:** These environment variables apply to the current PowerShell session. Set them again when opening a new terminal.

### 4. Apply Database Migrations

From the `backend` directory, run:

```powershell
python manage.py check
python manage.py migrate
```

### 5. Run the Backend

```powershell
python manage.py runserver
```

The Django development server is normally available at:

http://127.0.0.1:8000/

### 6. Set Up the Frontend

Open a separate terminal at the project root:

```powershell
cd frontend
npm install
npm run dev
```

Open the local URL displayed in the Vite terminal.

## Development Status

This project is actively being developed. Database models, API endpoints, frontend pages, and backend/frontend integration may change during development.

## Contributing

Suggestions, bug reports, and improvements are welcome. Please open an issue to discuss significant changes before submitting a pull request.

## License

No license has been specified yet.
