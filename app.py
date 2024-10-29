from flask import Flask, render_template, request, redirect, url_for

# Initialize a new Flask application
app = Flask(__name__)

# A simple in-memory list to store tasks (just for this example; no database here)
tasks = []

# Route for the homepage, displays the list of tasks
@app.route('/')
def index():
    # Render the 'index.html' template, passing the list of tasks
    return render_template('index.html', tasks=tasks)

# Route to handle adding a new task via a POST request
@app.route('/add', methods=['POST'])
def add_task():
    # Get the task description from the form input
    task = request.form.get('task')
    if task:
        # Append a new task to the list with a 'done' status as False
        tasks.append({'title': task, 'done': False})
    # Redirect back to the homepage after adding the task
    return redirect(url_for('index'))

# Route to delete a task based on its ID in the list
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    # Check if the task_id is valid
    if 0 <= task_id < len(tasks):
        # Remove the task from the list
        tasks.pop(task_id)
    # Redirect back to the homepage after deletion
    return redirect(url_for('index'))

# Route to toggle a task's completion status
@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    # Check if the task_id is valid
    if 0 <= task_id < len(tasks):
        # Toggle the 'done' status for the task
        tasks[task_id]['done'] = not tasks[task_id]['done']
    # Redirect back to the homepage after updating
    return redirect(url_for('index'))

# Start the Flask development server if running this script directly
if __name__ == '__main__':
    app.run(debug=True)
