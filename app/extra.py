from werkzeug import generate_password_hash, check_password_hash
import sqlite3
import datetime

@app.route("/")
def home():
	return render_template('index.html')

@app.route('/signup')
def new_user():
        if request.method =='POST':
                try:
                        email = request.form['inputEmailUp']
                        password = request.form['inputPasswordUp1']
                        hashed_password = generate_password_hash(password)

                        with sql.connect("database.db") as con:
                                cur = con.cursor()
                                cur.execute("INSERT INTO users (email,password) VALUES (?,?)",(email,password))

                                con.commit()
                                msg = "Record successfully added"
                except:
                        con.rollback()
                        msg = "error in insert operation"
                finally:
                        return render_template("result.html", msg = msg)
                        con.close()
                                            
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
