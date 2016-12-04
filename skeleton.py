def board(ip, port, sockobj, thiscommhandle, listencommhandle):
  msgheader = sockobj.recv(1024) # Receive message, 
  # React depending on message type: HTTP GET or POST, or some other type of communication.
  if msgheader.startswith( 'GET' ):
    htmlresponse = """<html>...</html>"""
    sockobj.send("HTTP/1.1 200 OK\r\nContent-type: text/html\r\n" + \
    "Content-length: %i\r\n\r\n%s" % (len(htmlresponse), htmlresponse))
    stopcomm(thiscommhandle)   
  elif msgheader.startswith( 'POST' ):
  	print "FEEL FREE TO CHANGE THE CODE"
  else:
  	print "FEEL FREE TO CHANGE THE CODE"
    
	
if callfunc == 'initialize':
  if len(callargs) > 1:
    raise Exception("Too many call arguments")

  # Running remotely (assuming that we pass input argument only remotely):
  # whenever this vessel gets a connection on its IPaddress:Clearinghouseport it'll call function board
  elif len(callargs) == 1:
    port = int(callargs[0])
    ip = getmyip()

  # Running locally:
  # whenever we get a connection on 127.0.0.1:12345 we'll call board
  else:
    port = 12345
    ip = '127.0.0.1'
  listencommhandle = waitforconn(ip,port,board)
