from flask import Flask,render_template
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
	title = 'intro'

	names = {"name": "Wan", "": "", "": "", "": ""}
	items = [{"text":"one"},{"text":"two"},{"text":"tree"},{"text":"four"},{"text":"five"},]

	return render_template('var-if-loops-extends.html', 
		names=names, 
		language='Python', 
		lang='', 
		framework='Flask',
		items=items)

if __name__=='__main__':
	app.run(debug=True, port=5000)