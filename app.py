from flask import Flask, redirect, render_template, request
app = Flask(__name__, template_folder="templates")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    port = int(5000)
    app.run(host='0.0.0.0', port=port, debug=True)



# from flask_mail import Mail, Message

# app = Flask(__name__, template_folder="templates")
# app.config["MAIL_DEFAULT_SENDER"] = "julian.layton@gmail.com"
# app.config["MAIL_PASSWORD"] = "yrvvwcvuhvbvcayi"
# app.config["MAIL_PORT"] = 587
# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_USE_TLS"] = True
# app.config["MAIL_USERNAME"] = "julian.layton"
# mail = Mail(app)

# REGISTRANTS = {}

# PROFESSION = [
#     "Business Analyst",
#     "Data Analyst",
#     "Front End Dev",
#     "Back End Dev",
#     "Infrastructure Eng",
#     "DevOps"
# ]

# @app.route("/")
# def index():
#     return render_template("index.html", profession=PROFESSION)

# @app.route("/register", methods={"POST"})
# def register():
#     email = request.form.get("email")
#     if not email:
#         return render_template("error.html", message="Missing email")
#     profession = request.form.get("profession")
#     if not profession:
#             return render_template("error.html", message="Missing profession")
#     if profession not in PROFESSION:
#         return render_template("error.html", message="Invalid profession")

#     REGISTRANTS[email] = profession

#     message = Message("You are registered!", recipients=[email])
#     mail.send(message)

#     return redirect("/registrants")

# @app.route("/registrants")
# def registrants():
#     return render_template("registrants.html", registrants=REGISTRANTS)

    # if not request.form.get("name") or request.form.get("profession") not in PROFESSION:
    #     return render_template("failure.html")
    # return render_template("success.html")


    # @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "GET":
#         return render_template("index.html")
#     if request.method == "POST":
#         return render_template("greet.html", name=request.form.get("name", "world"))
    
# @app.route("/index")
# def index():
#     if not request.form.get("name") or not request.form.get("Profession"):
#         return render_template("failure.html")
#     return render_template("index.html")

# @app.route("/register", methods=["POST"])
# def register():
#     return render_template("greet.html")