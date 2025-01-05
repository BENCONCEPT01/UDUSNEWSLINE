from flask import Flask, render_template, request
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Function to connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect('news.db')  # Ensure the database path is correct
        conn.row_factory = sqlite3.Row
        print("Database connection successful.")
        return conn
    except sqlite3.Error as e:
        print(f"Database connection failed: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    news = []

    if request.method == 'POST':
        search_query = request.form.get('search', '').strip()
        print(f"Search Query: '{search_query}'")  # Debugging

        if search_query:
            try:
                query = """
                SELECT id, title, content 
                FROM news 
                WHERE title LIKE ? OR content LIKE ? 
                ORDER BY id DESC
                """
                news = conn.execute(query, (f'%{search_query}%', f'%{search_query}%')).fetchall()
                print(f"Number of Results Found: {len(news)}")  # Debugging
            except Exception as e:
                print(f"Error executing query: {e}")
        else:
            print("Search query is empty.")
    else:
        print("GET request received; no search executed.")

    conn.close()
    return render_template('index.html', news=news)

if __name__ == '__main__':
    app.run(debug=True)
