from flask import Flask, jsonify, request
app = Flask(__name__)

empDB = [
{
	'id' : '101',
	'name' : 'Saravanan S',
	'title' : 'Technical Leader' 
},
{
	'id' : '201',
	'name' : 'Rajkumar P',
	'title' : 'Sr Software Engineer'
}
]

# get all
@app.route('/empDB/employee', methods = ['GET'])
def getAllEmp():
	return jsonify({'emps' : empDB})
'''
In the above code snippet, we have created a URI named '/empdb/employee' and also 
we defined the method as "GET". To service the GET call for the URI, Flask will 
call the function getAllEmp().  It will in turn simply call the "jsonify" method 
with employeeDB as the argument.  The "jsonify" is a flask method, will set the 
data with the given JSON object which is passed as a Python dictionary and set the
headers appropriately, in this case "Content-type: application/json".
'''

# get specific - using empID
@app.route('/empDB/employee/<empID>', methods = ['GET'])
def getEmp(empID):
	usr = [ emp for emp in empDB if (emp['id'] == empID) ]
	return jsonify({'emp' : usr})
'''
The above code will find the employee object with the given id and send 
the JSON object in the data. Here I have used the list comprehension technique
in Python if you don't understand you can simply write in an imperative way of 
processing the entire dictionary using a for loop.
'''

# PUT - to update an existing resource
@app.route('/empDB/employee/<empID>', methods = ['PUT'])
def updateEmp(empID):
	em = [ emp for emp in empDB if (emp['id'] == empID) ]
	#return em
	if 'name' in request.json:
		em[0]['name'] = request.json['name']

	if 'title' in request.json:
		em[0]['title'] = request.json['title']

	return jsonify({'emp' : em[0]})
'''
The above code gets the employee id from the URL and finds the respective object.
It checks the request.json from the request for the new data & then it overwrites 
the existing. NOTE: the request.json will contain the JSON object set in the client request.
We can also use a Postman client or cUrl to update an existing employee.  The data 
must contain the JSON object either with a name or title.The service can be invoked 
as follows in cUrl.  Here we update the "title" for employee id 201 with "Technical Leader". 
The request is responded with employee JSON object with updated values.  It also updates the employee DB.
=======for curl use this=====
curl -i -H "Content-type: application/json" -X PUT -d "{\"title\":\"Technical Leader\"}" http://127.0.0.1:5000/empDB/employee/201
'''

# POST - to create a new employee inside the database
@app.route('/empDB/employee', methods = ['POST'])
def createEmp():
	dat = {
	'id' : request.json['id'],
	'name' : request.json['name'],
	'title' : request.json['title']
	}
	empDB.append(dat)
	return jsonify(dat)
'''
The above code simply reads the request.json for the expected values, and stores 
them in the local dictionary object and appends it to the employee DB dictionary.
This also returns the newly added employee object as the response.
'''

# DELETE - to delete an employee
@app.route('/empDB/employee/<empID>', methods = ['DELETE'])
def deleteEmp(empID):
	em = [ emp for emp in empDB if (emp['id'] == empID)]
	if len(em) == 0:
		abort(404)

	empDB.remove(em[0])
	return jsonify({'response' : 'Success'})


@app.route("/")
def hello():
	return "Hello World!"

if __name__ == "__main__":
	app.run()
