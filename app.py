from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

base_path = r"C:\Users\David\Desktop\test"

@app.route("/", methods = ['GET','POST'])
def hello_world():
    path = os.listdir(path=base_path)

    if request.method == 'POST':
        files = request.form.getlist('selected_files')
        del_files(files)
        return redirect(url_for('hello_world'))

    return render_template('index.html', files=path) 

 
@app.route("/logs")
def show_logs():
    with open("logs.txt", "r") as file:
        return file.read()


def del_files(files):
    with open("logs.txt", "a") as log:
        for file in files:
            delete_me = os.path.join(base_path, file)
            if os.path.exists(delete_me):
                os.remove(delete_me)
                msg = f'File "{file}" deleted.\n'
            else:
                msg = f'File "{file}" DNE.\n'

            log.write(msg)
            print(msg.strip())