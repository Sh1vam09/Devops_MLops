from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

activities = [
    {"id": 1, "date_str": "28th Jan 2026", "time": "09:30", "completed": True, "tags": ["System Design", "Architecture"], "notes": "Drafted the high-level architecture for the real-time notification service."},
]

@app.route('/')
def index():
    return render_template('index.html', title="Activity History", activities=reversed(activities))

@app.route('/add', methods=['POST'])
def add_activity():
    date_val = request.form.get('date')
    time_val = request.form.get('time')
    subject = request.form.get('subject') 
    
    tags_str = request.form.get('tags', '')
    tags = [t.strip() for t in tags_str.split(',') if t.strip()]
    
    notes = request.form.get('notes')
    completed = 'completed' in request.form
    
    try:
        dt = datetime.strptime(date_val, '%Y-%m-%d')
        day = dt.day
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]
        formatted_date = dt.strftime(f"%-d{suffix} %b %Y")
    except:
        formatted_date = date_val 
        
    new_id = len(activities) + 1
    new_activity = {
        "id": new_id,
        "date_str": formatted_date,
        "time": time_val,
        "completed": completed,
        "tags": tags,
        "notes": notes
    }
    
    activities.append(new_activity)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
