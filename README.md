Ezipcode
====

Easy Brazilian zipcode (CEP) service (http://ezipcode.herokuapp.com)

[![Build Status](https://travis-ci.org/jairojair/ezipcode.svg?branch=dev)](https://travis-ci.org/jairojair/ezipcode)
[![Coverage Status](https://coveralls.io/repos/github/jairojair/ezipcode/badge.svg?branch=dev)](https://coveralls.io/github/jairojair/ezipcode?branch=dev)


## Using API

	Return all zipcodes 
	GET http://ezipcode.herokuapp.com/zipcode/

	Create zipcode 
	POST http://ezipcode.herokuapp.com/zipcode/

	Example body request format: {"zip_code": "14020260"}

	Return all zipcodes by limit
	GET http://ezipcode.herokuapp.com/zipcode/?limit=2

	Return data about specific zipcode
	GET http://ezipcode.herokuapp.com/zipcode/14020260/

	Delete zipcode 
	DELETE http://ezipcode.herokuapp.com/zipcode/14020260/ 


### Setup
	$ docker-compose build

### Runnings Tests
	$ docker-compose run dev make tests

### Running App
	$ docker-compose up

### API Access
	# http://0.0.0.0:5000/zipcode/
