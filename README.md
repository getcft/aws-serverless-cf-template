# aws-serverless-cfn-template

Serverless AWS CloudFormation template leveraging Lambda and API Gateway

## Description

This AWS CloudFormation template creates a AWS Lambda Serverless application which outputs generic JSON data sitting behind AWS API Gateway to handle a RESTful HTTP call via curl or a web browser. This Serverless application example can be useful when natively creating Serverless endpoints through CloudFormation. Other tools exist to do similar like serverless.com or Zappa which also allow for more end to end development built in. This however is meant to be as simplistic as possible just leveraging CloudFormation.

## Components

### serverless-cft.yaml

This CloudFormation template written in YAML format states where the Lambda application exists, what it is named along with some configuration settings such as memory allocated, timeout for the application, runtime interpreter, and also creates an API Gateway endpoint with the proper handling of HTTP response codes in concert with the Lambda application.

**Things to change or note**

* Change your S3Bucket to the name of your bucket where you put the lambda.zip
* Change the role name in two places from "role/serverless" to the role name you created
* To test use the URL provided in the Outputs under TestURL in a browser

### lambda-app.zip

This is a compressed zip file of lambda-app.py which is a simple function which when called outputs hard coded JSON. Lambda reads this zip file and uses the designated interpreter to execute it. In this example we are using Python as our language and the Python interpreter.
