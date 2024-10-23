from flask import Flask, render_template, redirect, request, flash, url_for

calculator = Flask(__name__)
calculator.secret_key = "sjsjdiueieuoiedpoewipoew"

sum_2 = []

@calculator.route('/')
def home():
    return render_template('index.html')

@calculator.route('/sum_of_two_numbers', methods=['GET', 'POST'])
def sum_of_two_numbers():
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
        
        number_x = int(number_x)
        number_y = int(number_y)
        
        sum_2.append(number_x)
        sum_2.append(number_y)
        
        result = sum(sum_2)
        
        flash(f'✅ Great job, you are a mathlete!\n{number_x} + {number_y} = {result}', 'success')
        return redirect(url_for('home'))
    
    return render_template('calculator.html')

if __name__ == '__main__':
    calculator.run(debug=True)
        
        
    
    
    