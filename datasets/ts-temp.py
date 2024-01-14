import httplib, urllib
import time
import Adafruit_DHT as dht
key = 'C4QLJ0EURKQ1VH5Y'  # Thingspeak channel to update

while True:
	h, t = dht.read_retry(11,4);.
	print "Temp:", t
	param = urllib.urlencode({'field1': t, 'key':key }) 
	head = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
	con = httplib.HTTPConnection("api.thingspeak.com:80")
	try:
		con.request("POST", "/update", param, head)
		response = con.getresponse()
		print response.status, response.reason
		data = response.read()
		con.close()
	except:
		print "connection failed"
