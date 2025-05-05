# AK-Express-App



A full-stack delivery management platform with a modern Angular frontend and a Node.js/Express/MongoDB backend.

---

## Table of Contents

1. [Overview](#overview)

2. [Features](#features)

3. [Technologies Used](#technologies-used)

4. [Installation](#installation)

5. [API Endpoints](#api-endpoints)

6. [Contributing](#contributing)

7. [License](#license)

---

## Overview

**AK-Express-App** is a delivery management system designed to streamline order creation, assignment, and tracking for vendors, admins, and delivery agents.

- **Frontend**: Built with Angular for a responsive, user-friendly interface.

- **Backend**: Built with Node.js, Express, and MongoDB, providing RESTful APIs for authentication and delivery management.

---

## Features

- User authentication (Register/Login)

- Role-based access (Admin, Vendor, Delivery Agent)

- Order creation and assignment

- Delivery agent management

- Order status updates and tracking

- JWT-based API security

---

## Technologies Used

### Frontend

- Angular 19

- Bootstrap 5

- RxJS

### Backend

- Node.js

- Express.js

- MongoDB (Mongoose)

- JWT for authentication

- bcryptjs for password hashing

- dotenv for environment variables

---

## Installation

### Prerequisites

- Node.js (v18+)

- npm

- MongoDB

### Backend Setup

```bash

cd backend

npm install

npm start

```

### Frontend Setup

```bash

cd frontend

npm install

ng serve

```

---

## API Endpoints

### Auth Routes

- `POST /api/auth/register` – Register a new user

- `POST /api/auth/login` – Log in

### Delivery Routes

- `POST /api/delivery/create` – Create a new order (Vendor/Admin)

- `GET /api/delivery/all` – Get all orders (Vendor/Admin)



- `GET /api/delivery/agents/all` – List all delivery agents (Vendor/Admin)

- `PUT /api/delivery/assign` – Assign an order (Admin only)

- `GET /api/delivery/my-orders/:userId` – Get orders for a delivery agent

- `PUT /api/delivery/status` – Update order status (DeliveryAgent)

**Note:** All routes are protected with JWT and require appropriate roles.

---

## License

This project is licensed under the MIT License.
