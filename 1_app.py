from flask import  Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "Thanks  i eam  from  watching "

@app.route('/users')
def users():
    return "Wlecome to users"
@app.route("/users/<name>")
def user(name):
    return f"Hi i am {name}"

@app.route("/student/<name>/<int:num>")
def userr(name,num):
    return f"Hello {name} nad {num}"

@app.route("/about") 
def about():
    return "Welcome to about Page"
@app.route("/contact")
def contact():
    return "*9965150"

if __name__=="__main__":
    app.run(debug=True)
