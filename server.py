import csv
from flask import Flask, render_template, request, redirect


# creating an instance of the class Flask
# the argument - the name of the application module or package
# __name__ - shortcut suitable for this ^^^
app = Flask(__name__)



# route decorator tells Flask which URL address should trigger
# the function below
@app.route("/")
# default value
def my_home():
	# render_template - method to generate any type of text files
	# in our case - index.html, and parameter we passing into it
    return render_template('index.html')

@app.route("/<string:page_name>")
# default value
def html_page(page_name):
	# render_template - method to generate any type of text files
	# in our case - index.html, and parameter we passing into it
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == "POST":
		data = request.form.to_dict()
		write_to_csv(data)
		return redirect("/contact_thank_you.html")
	else:
		return "somethong went wrong"


def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data["email"]
		name = data["name"]
		message = data["message"]
		file = database.write(f'{email}, {name}, {message}\n')

def write_to_csv(data):
	with open('database2.csv', mode='a', newline='\n') as database2:
		email = data["email"]
		name = data["name"]
		message = data["message"]
		file_writer = csv.writer(database2, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
		file_writer.writerow([email, name, message])



