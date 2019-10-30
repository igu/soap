from SOAPpy import SOAPProxy

server = SOAPProxy('http://localhost:8080/server.php')
print (server.getNomeEstudante('20181014040020'))
