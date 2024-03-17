import os
from werkzeug.utils import secure_filename
# from PIL import Image
# import PIL
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash


from helpers import login_required
# UPLOAD_FOLDER = os.getcwd() + '/app/static/images'
UPLOAD_FOLDER = os.path.join('static','images')

# Configure application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///cherrybeans.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():

    return render_template("index.html")
###########################################################buy###########################################
@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    purchases = db.execute("SELECT * FROM purchases")
    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        number= request.form.get("number")
        process = "شراء"
        db.execute("INSERT INTO purchases (user_id,name, number,price) VALUES (:user_id, :name, :number,:price)", user_id=session["user_id"], name=name,number=number, price=price)
        db.execute("INSERT INTO transactions (user_id,process,number,price) VALUES(?,?,?,?)",session["user_id"],process,number,price)
        return render_template("buy.html",purchases=purchases)
        # return redirect("/")
    else:
        return render_template("buy.html",purchases=purchases)
###########################################################history###########################################
@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("SELECT * FROM transactions ORDER BY timestamp DESC")

    return render_template("history.html",transactions=transactions)
    # ,transactions=transactions)

###########################################################login###########################################
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash("invalid username and/or password!")
            return render_template("login.html")
        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        flash(f"Welcome {rows[0]["username"]}!")
        # Redirect user to home page
        return render_template("index.html")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

###########################################################logout###########################################
@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()
    # Redirect user to login form
    return redirect("/")
###########################################################regester###########################################
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # return apology("TODO")
    if request.method == "POST":
        try:
            db.execute("INSERT INTO users (username,hash) VALUES(?,?)",request.form.get("username"), generate_password_hash(request.form.get("password")))
        except:
            flash("Username already use!")
            return render_template("register.html")
        return redirect("/")
    else:
        return render_template("register.html")

###########################################################sell###########################################
@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    orders = db.execute("SELECT * FROM orders")
    if request.method == "POST":
        try:
            refrenceId = db.execute("INSERT INTO transactions (user_id,process,number,price) VALUES(?,?,?,?)",request.form.get("user_id"), request.form.get("process")
                       ,request.form.get("number"),request.form.get("price"))
            # refrenceId = db.lastrowid
            # cart(refrenceId)
            print(refrenceId)
            # print(request.form.get("cart[0][item]"))
            for order in range(len(orders)) :
                # print(request.form.get("cart[",order,"][item]"))
                # x= request.form.get(f'cart[{order}][item]')
                # print(x)
                db.execute("INSERT INTO cart (r_id,price,number,item) VALUES(?,?,?,?)",refrenceId,request.form.get(f"cart[{order}][price]"),request.form.get(f"cart[{order}][number]"),request.form.get(f"cart[{order}][item]"))
            return render_template("sell.html",orders=orders)
        except:
            flash("ما مشي الحال")
            return render_template("sell.html",orders=orders)

        # return render_template("sell.html",orders=orders)
    else:
        return render_template("sell.html",orders=orders)

###########################################################setting###########################################
@app.route("/setting", methods=["GET", "POST"])
@login_required
def setting():
    if request.method == "POST":
        uploaded_img = request.files['uploaded-file']
        # Extracting uploaded data file name
        img_filename = secure_filename(uploaded_img.filename)
        print(img_filename)
        db.execute("INSERT INTO orders (item,price,sub,picName) VALUES(?,?,?,?)",request.form.get("item"),request.form.get("price"),request.form.get("sub"),img_filename)
        # Upload file to database (defined uploaded folder in static path)
        uploaded_img.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
        # Storing uploaded file path in flask session
        session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)
        flash("تمت إضافة المنتج على القائمة")
        return render_template("setting.html")
    else:
        return render_template("setting.html")
