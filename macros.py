from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	title = 'Macros'

	myList = [234, 235, 232, 466, 654, 875]
	moreNumbers = [634, 4362, 4672, 5745, 5356, 4532]

	return render_template('macros.html', 
		title=title,
		name='Wan', 
		numbers=myList, 
		moreNumbers=moreNumbers)

if __name__=='__main__':
	app.run(debug=True)