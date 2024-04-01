from flask import Flask, render_template, request
import re


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=["GET", "POST"])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matches = re.findall(regex_pattern, test_string)
    return render_template('results.html', matches=matches)

@app.route('/validate_email', methods=["GET", "POST"])
def validate_email():
    email = request.form['email']
    is_valid = '@' in email and '.' in email  # Basic check for presence of '@' and '.'
    return render_template('validate_email.html', is_valid=is_valid, email=email)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
