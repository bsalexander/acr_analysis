
from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure secret key

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        access_code = request.form.get('access_code')
        duke_netid = request.form.get('duke_netid')
        if access_code == 'Duke_EM':  # Replace with your desired access code
            session['logged_in'] = True
            session['duke_netid'] = duke_netid
            return redirect(url_for('form'))
        return render_template('login.html', error='Invalid access code')
    return render_template('login.html')

@app.route('/form', methods=['GET', 'POST'])
@login_required

def form():
    import csv
    from datetime import datetime
    scenarios = []
    scenario_ids = []
    with open('acr_ac_scenarios.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            if 'abdomen' in row[6].lower():
                scenarios.append(row[2])
                scenario_ids.append(row[1])
    scenarios = scenarios[:5]
    scenario_ids = scenario_ids[:5]
    
    if request.method == 'POST':
        responses = {}
        for i in range(len(scenarios)):
            response = request.form.get(f'vote_{i}') 
            responses[scenario_ids[i]] = response
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('response_log.txt', 'a') as log_file:
            log_file.write(f"{timestamp},{session['duke_netid']},{','.join([f'{id}:{responses[id]}' for id in scenario_ids])}\n")

        return 'Form submitted successfully!'
        
    return render_template('form.html', scenarios=scenarios, scenario_ids=scenario_ids, zip=zip)

if __name__ == '__main__':
    app.run(debug=True)
