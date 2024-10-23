from flask import Flask, render_template, redirect, request, flash, url_for
import mysql.connector

DATABASE_HOST = "localhost"
DATABASE_USER = "root"
DATABASE_PASSWORD = "m1a2i3L4$"
DATABASE_NAME = "calculator_db"

calculator = Flask(__name__)
calculator.secret_key = "sjsjdiueieuoiedpoewipoew"

# sum_2 = []

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host=DATABASE_HOST,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            database=DATABASE_NAME
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None

@calculator.route('/')
def home():
    return render_template('index.html')

@calculator.route('/sum_of_two_numbers', methods=['GET', 'POST'])
def sum_of_two_numbers():
    
    connection = connect_to_database()
    
    if connection is None:
        flash("Error: Unable to connect to the database", "danger")
        return render_template('calculator.html')
    
    if request.method == 'POST':
        number_x = request.form['number_x'].strip()
        number_y = request.form['number_y'].strip()
    
        errors = []
        
        if not number_x.isdigit():
            errors.append("X must be an integer!")
        
        if not number_y.isdigit():
            errors.append("Y must be an integer!")
        
        if errors:
            return render_template('calculator.html', errors=errors)
        
        # number_x = int(number_x)
        # number_y = int(number_y)
        
        result = int(number_x) + int(number_y)
        
        # result = sum(sum_2)
        
        try:
            # Insert into database
            cursor = connection.cursor()
            sql = "INSERT INTO calculations (number_x, number_y, result) VALUES (%s, %s, %s)"
            values = (number_x, number_y, result)
            cursor.execute(sql, values)
            connection.commit()
            
            flash(f'✅ Great job, you are a mathlete!\n{number_x} + {number_y} = {result}', 'success')
            return redirect(url_for('home'))
        except mysql.connector.Error as err:
            flash(f"Database error: {err}", "danger")
            return render_template('calculator.html')
        
        finally:
    
            # Close database connection
            if connection:
                cursor.close()
                connection.close()
    
    return render_template('calculator.html')

if __name__ == '__main__':
    calculator.run(debug=True)
        
        
    
    
    