# PyFlaskWebService
Note: This is just for the understanding purpose of RESTful webservice.

The idea is to develop a RESTful Web Service in Python using Flask.

RESTful Web Service is an architectural style, where the data or the structural components of a system is described 
in the form of URI ( Uniform Resource Identifier) and the behaviors are described in terms of methods. The resources
can be manipulated using CRUD (Create, Read, Update and Delete) operations. The communication protocol
for REST is HTTP since it suits the architecture requirement of being a stateless communication across the Client and Server.

THE PLAN:

The plan is to create an in-memory JSON DB to store and manipulate a simple employee database and
develop RESTful APIs to perform CRUD operations using GET, POST, PUT, and DELETE methods.

>GET  /empdb/employee/            - Retrieve all the employees from the DB

>GET /empdb/employee/             - Retrieve the details of given employee Id

>POST /empdb/employee/            - Create a record in the employee DB, whereas the employee details are sent in the request as a JSON object

>PUT /empdb/employee/             - Update the employee DB, with the given details of employee in the data part as a JSON object

>DELETE /empdb/employee/          - Delete the employee from the DB for the employee Id.

As for the database, will create a dictionary to hold a JSON objects for a couple of employee records
and then will add the RESTful APIs for each supported operations.

EXECUTION:

When running the web server, one can open their web browser and check the web server. The server is available in the URL http://localhost:5000/ or else if familiar with cUrl then can also execute the below to check the status:

GET methods

> $ curl -i http://localhost:5000/

> $ curl -i http://localhost:5000/empDB/employee

> $ curl -i http://localhost:5000/empDB/employee/201

PUT method

> $ curl -i -H "Content-type: application/json" -X PUT -d "{\"title\":\"Technical Leader\"}" http://localhost:5000/empDB/employee/201

DELETE method

> $ curl -i -X DELETE http://localhost:5000/empDB/employee/201

POST method

> $ curl -i -H "Content-type: application/json" -X POST -d "{\"id\":\"301\",\"name\":\"Rama\",\"title\":\"manager\"}"

or else could also use browser plugins like POSTMAN for the CRUD operations on RESTful web service.
