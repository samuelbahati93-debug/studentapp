from flask import Flask, request, jsonify, render_template
import psycopg2

app = Flask(__name__)

# 🔗 Connect to Supabase PostgreSQL
def connect_db():
    return psycopg2.connect(
        host="db.uhqwblobwtcrgdzzjkpg.supabase.co",
        database="postgres",
        user="postgres",
        password="asKnN2Beg2PRjyrn",  # 🔥 replace this
        port="5432"
    )

# 🏠 Home page
@app.route("/")
def home():
    return render_template("index.html")

# ➕ Add student
@app.route("/add", methods=["POST"])
def add_student():
    data = request.json

    try:
        conn = connect_db()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO students 
            (regno, secondname, surname, course, county, gender, department, school)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            data["regno"],
            data["secondname"],
            data["surname"],
            data["course"],
            data["county"],
            data["gender"],
            data["department"],
            data["school"]
        ))

        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"status": "success"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# ▶ Run app locally
if __name__ == "__main__":
    app.run(debug=True)