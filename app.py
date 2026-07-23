from flask import Flask, render_template

app = Flask(__name__, template_folder='app/tamplates')
app.config.from_object('config.Config')

@app.route('/')
def dashboard():
    # Dữ liệu mẫu dựng sẵn khớp với giao diện thực tế
    stats = {
        'total_employees': 25,
        'total_tasks': 18,
        'total_schedules': 62,
        'working_today': 12
    }
    return render_template('index.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)