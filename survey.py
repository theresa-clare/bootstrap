from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    """Show index page."""
    return render_template("survey.html")


@app.route('/profile', methods=['POST'])
def profile():
    """Return results from profile form."""

    fullname = request.form['name']
    age = request.form['age']
    occupation = request.form['occupation']
    salary = request.form['salary']
    education = request.form['education']
    state = request.form['state']
    city_type = request.form['city']
    garden = request.form['garden']
    tv = request.form['tv']

    return jsonify({'fullname': fullname, 'age': age, 'occupation': occupation,
                    'salary': salary, 'education': education, 'state': state,
                    'city_type': city_type, 'garden': garden, 'tv': tv})


if __name__ == "__main__":
    app.run(debug=True)