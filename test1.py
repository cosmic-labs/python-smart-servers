#Python Smart Server Test 1 by Cosmic Labs

#Info: GREEN

def runserver(PORT):

  import SimpleHTTPServer
  import SocketServer
  
  Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
  
  httpd = SocketServer.TCPServer(("", PORT), Handler)
  
  print "serving at port", PORT
  httpd.serve_forever()
