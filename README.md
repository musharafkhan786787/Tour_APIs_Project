# 🧭 TourApp API

A RESTful API for managing travel locations and user bookings, built with Django REST Framework. Includes secure user authentication (JWT), password reset via email, and admin-managed locations.

---

## 🚀 Features

### 🔐 Authentication & Security
- User Signup with email, username, and password
- JWT-based login with access/refresh token
- Password reset via email using token (via `rest_registration`)
- Custom user model with email as the login field

### 🌍 Location Management
- Admins can create/update/delete locations
- Authenticated users can view/search all locations
- Locations include: `name`, `description`, `price`, `images`, and external `url`

### 📆 Booking System
- Authenticated users can book any available location
- Bookings are linked to both user and location
- Users can view only their own bookings
- Admins can view all bookings via admin panel

### 🛠 Tech Stack
- Python 3.13
- Django 5.1
- Django REST Framework
- SimpleJWT for token-based authentication
- rest_registration for easy auth/reset endpoints

---

## 🔐 Authentication & Registration Flow

This project uses:
- `rest_registration` for registration, reset password,
- `SimpleJWT` for secure login tokens

## 📁 Project Structure
  
Authproject/
├── accounts/       # Custom user model & auth
├── bookings/       # Booking API
├── locations/      # Location API
├── Authproject/    # Main project settings
└── db.sqlite3  

##🔧 Setup Instructions
#Clone the repository

git clone https://github.com/musharafkhan786787/Tour_APIs_Project.git
cd Tour_APIs_Project

🤝 Contributing
Contributions, suggestions, and improvements are welcome!
Feel free to fork the repository and submit a pull request.
