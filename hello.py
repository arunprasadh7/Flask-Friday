from flask import Flask,render_template

# Create a Flask instance 
app = Flask(__name__)

# Create a route decorator 
@app.route('/')
# def index():
#     return '<h1>Hello Arun!!!!</h1>'

def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello {name}</h1>'

# routing to First page 
@app.route('/first/<name>')
def first(name):
    return render_template('first.html',user_name=name)

#routing to second page 
@app.route('/second')
def second():
    return render_template('second.html')

# Using Jinja templates for variables 
@app.route('/job/<name>')
def job(name):
    course =  'Python'
    fruits = ['apple','orange','mango','banana','kiwi']
    return render_template('job.html',user_name=name,course=course,fruits=fruits)


#Dota auto lane assigner 
@app.route('/dota/<int:position>')
def dota_lane(position):
    roles = ['Carry','Mid','Offlane','Soft support','Hard support']
    return render_template('dotalanes.html',position=position,roles=roles)

# Creating custom error handling pages 

# Invalid URL - 404 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

# Internal Server error - 500
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html')




# Enabling debugger and running app 
if __name__ == '__main__':
    app.run(debug=True)