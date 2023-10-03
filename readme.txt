This is a full stack project for a grocery delivery system. The project is built using React, Flask, and SQLite.

Installation
1.Clone the repository:

git clone https://github.com/username/grocery-delivery-system.git

2. Install the dependencies for the frontend:

cd grocery-delivery-system/frontend
npm install

3. Install the dependencies for the backend:
cd ../backend
pip install -r requirements.txt

Flask==2.0.1
Flask-Cors==3.0.10
Flask-RESTful==0.3.9
SQLAlchemy==1.4.22

4. Create the database:

cd ../database
sqlite3 grocery.db < schema.sql
sqlite3 grocery.db < seed.sql

Usage
Start the backend server:
cd ../backend
python app.py

Start the frontend server:

cd ../frontend
npm start

Open the application in your web browser:

http://localhost:3000/

Testing
Run the unit tests for the backend:
cd ../tests
pytest




