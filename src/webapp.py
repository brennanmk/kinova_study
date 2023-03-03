from flask import Flask, render_template, request
from study_controller import study_controller
app = Flask(__name__)

controller = study_controller.study_controller()


@app.route('/', methods = ['POST', 'GET'])
def robots():
    if request.method == 'POST':
        if 'view_one' in request.form:
            controller.addEntry(1)
        elif 'view_two' in request.form:
            controller.addEntry(2)
        elif 'view_three' in request.form:
            controller.addEntry(3)
        elif 'view_four' in request.form:
            controller.addEntry(4)
        elif 'view_five' in request.form:
            controller.addEntry(5)
        elif 'view_six' in request.form:
            controller.addEntry(6)
        elif 'view_seven' in request.form:
            controller.addEntry(7)
        elif 'view_one' in request.form:
            controller.disp_grasp(1)
        elif 'view_two' in request.form:
            controller.disp_grasp(2)
    return render_template("index.html")
    
if __name__ == '__main__':
    app.run()
