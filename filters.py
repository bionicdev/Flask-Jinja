from flask import Flask, render_template
app = Flask(__name__)


def customFilter2(x, y):
	return x * y

app.jinja_env.filters['customFilter2'] = customFilter2


def customFilter(x, y):
	return x ** y

app.jinja_env.filters['customFilter'] = customFilter		


def reverse(string):
	return string[::-1]

app.jinja_env.filters['reverse'] = reverse


def myFunction(var):
	return var + 3


@app.route('/')
def index():
	title = 'Filters'

	return render_template('filters.html', 
		title=title, 
		myVar=-3,
		myDict={'firstKey': 'test value 1', 'secondKey': 'test value 2'},
		myNumberList=[1,2,3,4,5],
		myNumber = 10,
		testVar='test string',
		myFunction=myFunction,
		)

if __name__=='__main__':
	app.run(debug=True)