from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def grade_analyzer():
    result = ''
    error = ''

    if request.method == 'POST':
        try:
            # Get the marks from form inputs
            mark1 = float(request.form.get('mark1'))
            mark2 = float(request.form.get('mark2'))
            mark3 = float(request.form.get('mark3'))

            # Calculate total and average
            total = mark1 + mark2 + mark3
            average = total / 3

            # Determine grade
            if average >= 90:
                grade = 'A'
            elif average >= 75:
                grade = 'B'
            elif average >= 50:
                grade = 'C'
            else:
                grade = 'Fail'

            result = f"Total: {total}, Average: {average:.2f}, Grade: {grade}"

        except:
            error = "Please enter valid numbers only."

    return f'''
        <h2> Student Grade Analyzer </h2>
        <form method="POST">
            Subject 1 Marks: <input type="text" name="mark1" required><br><br>
            Subject 2 Marks: <input type="text" name="mark2" required><br><br>
            Subject 3 Marks: <input type="text" name="mark3" required><br><br>
            <button type="submit">Calculate</button>
        </form>
        <h3 style="color: green;">{result}</h3>
        <h3 style="color: red;">{error}</h3>
    '''

if __name__ == "__main__":
    app.run(debug=True)

