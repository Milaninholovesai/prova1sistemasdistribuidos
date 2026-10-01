Arquivo cliente.py:

from xmlrpc.cliente import ServerProxy



servidor = ServerProxy("http://localhost:8004/")



resultado = servidor.calcular_pontos(120, 2)



print("Pontos recebidos:", resultado)
