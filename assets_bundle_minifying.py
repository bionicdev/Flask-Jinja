from flask import Flask,render_template
from flask_assets import Bundle, Environment


app = Flask(__name__)

js = Bundle('home.js', 'add.js', 'subtract.js', output='gen/main.js', filters='jsmin')
css = Bundle('main.css', 'style.css', output='gen/main-style.css', filters='cssmin')
assets = Environment(app)
assets.register('main_js', js)
assets.register('main_css', css)

@app.route('/')
def index():
	title = 'Assets'

	return render_template('assets.html', title=title)

if __name__=='__main__':
	app.run(debug=True)