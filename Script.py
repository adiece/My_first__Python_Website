from flask import Flask  # importing Flask object from  flask class
from flask import render_template  # it accessed html files used in python script and display it

app = Flask(__name__)


@app.route('/')  # / means homepage
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)

# Virtual env creation in python , by creating virtual env we can
# pip install virtualenv
# python -m venv virtual(virtual is name of virtual env folder)
# login to heroku from demo folder where your scrip is ---heroku login # email-adiece002@gmail.com,Python@123
# create heroku folder  --heroku create adiece   --  https://git.heroku.com/adiece.git
# heroku apps to see your app list
# from virtula/scripts -- pip install gunicorn
# pip freeze to list the libraries install in python virtual env.
# pip freeze > requirement.txt -- for putting libraries in a text file
# gunicorb is library that heroku needs to run the program on HTTP server.
# git init to initialize the git in your folder
# git add . to add file in git repositry
# git commit -m "first commit" to make the changes
# set git remote heroku to https://git.heroku.com/adiece.git
# heroku git:remote --app adiece to point the to my app adiece
