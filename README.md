# TechStore Management System

A web-based technology store management system designed to support product management, inventory tracking, shopping cart operations, and order processing.

## Overview

**TechStore Management System** is a full-stack web application developed to organize the core operations of an online technology store. The project separates the backend and frontend to support maintainability and future expansion.

The system is currently under development.

## Tech Stack

### Backend

* Python
* Django
* MySQL

### Frontend

* React
* Vite
* TypeScript

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
│   └── manage.py
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
├── .gitignore
└── README.md
```

## Planned Features

* User and customer management
* Product, category, and brand management
* Product variants and product images
* Shopping cart and cart item management
* Order and order item management
* Payment and shipment management
* Inventory tracking and inventory transactions
* Supplier and purchase order management
* Promotion management

Additional features may be introduced as development progresses.

## Getting Started

### Prerequisites

Install the following tools before running the project:

* Python
* Node.js and npm
* MySQL Server
* Git

### 1. Clone the Repository

```bash
git clone https://github.com/dtl2811/TechStore-Management-System.git
cd TechStore-Management-System
```

### 2. Set Up the Backend

Create and activate a Python virtual environment from the project root.

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
cd backend
pip install django mysqlclient
```

Install any additional dependencies required by the project if necessary.

### 3. Configure the Database

Create a MySQL database named `techstore`.

Configure the database connection using environment variables:

* `DB_USER`
* `DB_PASSWORD`
* `DB_HOST`
* `DB_PORT`

Do not commit database passwords, secret keys, or other sensitive credentials to the repository.

### 4. Run the Backend

From the `backend` directory:

```bash
python manage.py migrate
python manage.py runserver
```

The Django development server normally runs at:

```text
http://127.0.0.1:8000/
```

### 5. Set Up the Frontend

Open another terminal from the project root:

```powershell
cd frontend
npm install
npm run dev
```

Open the local URL displayed by Vite in the terminal.

## Development Status

This project is actively being developed. Features, database models, and application integration may change as development continues.

## Contributing

Suggestions, bug reports, and improvements are welcome. Please open an issue to discuss significant changes before submitting a pull request.

## License

No license has been specified yet.
