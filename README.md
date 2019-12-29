Applying Model checkpoint. 

* Clone the repo and run the below command on your Linux machine 

1. Open Terminal on Linux and Run:
   # python server.py

2. Open another terminal and run below command:
   # curl -XPOST http://localhost:8080/api -H 'Content-Type: application/json' -d @test_data.json

3. In order to make prediction using request:
   # python request.py