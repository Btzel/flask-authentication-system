# Flask Authentication System
A secure user authentication system built with Flask, featuring user registration, login functionality, and protected file downloads.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-red)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-Database-green)
![Security](https://img.shields.io/badge/Authentication-SHA256-orange)

## 🎯 Overview
A basic authentication system that provides:
1. User registration and login functionality
2. Basic password hashing with salt generation
3. Protected route access control
4. Simple file download protection
5. Session-based authentication

The system implements fundamental security practices and serves as a foundation for authentication. For production use, additional security features such as password policies, email verification, rate limiting and more can be implemented.

## 🔒 Security Features
### Authentication System
- Password hashing with salt
- Session management
- Protected routes
- Secure file downloads
- User verification

### User Management
- Email validation
- Unique user checking
- Login state tracking
- Logout functionality
- Session persistence

## 🔧 Technical Components
### Authentication Implementation
```python
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        user = db.session.execute(db.select(User)
                    .where(User.email == email)).scalar()
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('secrets'))
```

### Key Features
1. **User Security**
   - Password hashing
   - Salt generation
   - Session handling
   - Route protection

2. **Database Management**
   - User model
   - Email uniqueness
   - Data persistence
   - Query handling

3. **Access Control**
   - Protected downloads
   - Login required routes
   - Authentication checks
   - Session tracking

## 💻 Implementation Details
### Project Structure
- Flask application core
- SQLAlchemy database
- Flask-Login integration
- Template inheritance

### Database Model
```python
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
```

## 🚀 Usage
1. Install required packages:
```bash
# Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

2. Set up environment variable:
```bash
export API-KEY="your-secret-key"
```

3. Run the application:
```bash
python main.py
```

## 📦 Requirements
- Python 3.13.1
- Flask==3.1.0
- Flask-Login==0.6.3
- Flask-SQLAlchemy==3.1.1
- Werkzeug==3.1.3
- SQLAlchemy==2.0.37

View full requirements in `requirements.txt`

## 🎯 Features
### User Authentication
- Secure registration
- Login system
- Password protection
- Session management

### Route Protection
- Login required decorator
- User verification
- Protected downloads
- Secure redirects

## 🛠️ Project Structure
```
flask-auth/
├── main.py           # Application core
├── templates/        # HTML templates
│   ├── base.html    # Base template
│   ├── index.html   # Home page
│   ├── login.html   # Login form
│   ├── register.html # Registration
│   └── secrets.html # Protected page
├── static/          
│   ├── css/         # Stylesheets
│   └── files/       # Protected files
└── instance/        
    └── users.db     # SQLite database
```

## 📊 Security Measures
### Password Protection
- SHA256 hashing
- Salt generation
- Secure storage
- Hash verification

### Access Control
- Route protection
- Session management
- Login validation
- Secure downloads

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author
Burak TÜZEL