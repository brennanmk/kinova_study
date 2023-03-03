from flask import Flask, render_template, request
import database
from study_controller import study_controller
app = Flask(__name__)

controller = database.dbController()

study_controller = study_controller()

@app.route('/', methods = ['POST', 'GET'])
def robots():
    if request.method == 'POST':
        if 'delete' in request.form:
            controller.delete(request.form["delete"], 'robots')
        elif 'update' in request.form:
            controller.update_robot_table(request.form["update"], request.form["name"], request.form["ip"], request.form["port"], request.form["image"])
        elif 'create' in request.form:
            controller.add_robot(request.form["name"], request.form["ip"], request.form["port"], request.form["image"], request.form["image_target_width"])
    return render_template("robots.html")

@app.route('/robot_data')
def robot_data():
    return controller.getData('robots')
    
if __name__ == '__main__':
    app.run()
