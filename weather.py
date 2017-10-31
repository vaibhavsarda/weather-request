# function to get weather response
def weather_response(location, API_key):
	import urllib.request
	c="http://api.openweathermap.org/data/2.5/forecast?q="
	e=c+location+'&APPID='+API_key
	data=urllib.request.urlopen(e).read().decode()
	return data
	# write your code 

# function to check for valid response 
def has_error(location,json):
	if json.find('"name":"'+location+'"')==-1 :
		return True
	else:	
		return False 

# function to get attributes on nth day
def get_temperature(json,n=0,t="3:00:00"):
	import datetime
	a=datetime.datetime.now().date()
	if n==0 :
		b=json.find(str(a)+' '+t)
	else :
		a+=datetime.timedelta(days=n)
		b=json.find(str(a)+' '+t)
	
	c=json[b-340:b]
	d=c.find("temp")
	e=float(c[d+6:d+11])
	
	return e

def get_humidity(json,n=0,t="3:00:00"):
	import datetime
	a=datetime.datetime.now().date()
	if n==0 :
		b=json.find(str(a)+' '+t)
	else :
		a+=datetime.timedelta(days=n)
		b=json.find(str(a)+' '+t)
	c=json[b-317:b]
	d=c.find("humidity")
	if c[d+13]==',':
		humidity=float(c[d+10:d+12])
	elif c[d+13]!=',':
		humidity=float(c[d+10:d+13])



	# write your code 
	return humidity

def get_pressure(json,n=0,t="3:00:00"):
	import datetime
	a=datetime.datetime.now().date()
	if n==0 :
		b=json.find(str(a)+' '+t)
	else :
		a+=datetime.timedelta(days=n)
		b=json.find(str(a)+' '+t)
	c=json[b-317:b]
	d=c.find("pressure")
	e=float(c[d+10:d+16])
	return e

def get_wind(json,n=0,t="3:00:00"):
	import datetime
	a=datetime.datetime.now().date()
	if n==0 :
		b=json.find(str(a)+' '+t)
	else :
		a+=datetime.timedelta(days=n)
		b=json.find(str(a)+' '+t)
	c=json[b-317:b]
	d=c.find("wind")
	e=float(c[d+15:d+18])
	return e 
	

def get_sealevel(json,n=0,t="3:00:00"):
	import datetime
	a=datetime.datetime.now().date()
	if n==0 :
		b=json.find(str(a)+' '+t)
	else :
		a+=datetime.timedelta(days=n)
		b=json.find(str(a)+' '+t)
	c=json[b-317:b]
	d=c.find("sea_level")
	e=float(c[d+11:d+16])
	return e
	# write your code
	




