Prova 1 de Sistemas Distribuidos

Nome: Mayran Juvenal milani
RA: cb94b75b8d0828c19239

Problema da Empresa: 
-Nos foi solicitado esse calculo pois nesta loja eles concedem pontos de fidelidade ao clientes por real gasto mas não queriam ter que calcular compras grandes como por exemplo R$120, o servidor fara o calcula para a loja de forma automatizada.

Arquivos: 
Arquivo servidor.py:

from xmlrpc.server import SimpleXMLRPCServer


def calcular_pontos(valor_compra, pontos_por_real):

    return valor_compra * pontos_por_real



    servidor = SimpleXMLRPCServer(("localhost", 8004))


    servidor.register_function(
        calcular_pontos,
        "calcular_pontos"
    )


print("Servidor RPC aguardando solicitações...")


servidor.serve_forever()
(recebe a chamada RPC e executa o cálculo)


Cliente py

Arquivo cliente.py:

from xmlrpc.cliente import ServerProxy



servidor = ServerProxy("http://localhost:8004/")



resultado = servidor.calcular_pontos(120, 2)



print("Pontos recebidos:", resultado)




Resultado do teste: 


Pontos recebidos: 240


explicação

1. O cálculo foi executado no programa servidor, ou seja, no arquivo servidor.py.

2. A solicitação foi iniciada pelo cliente.py.

3. Se o servidor estiver desligado, o cliente.py tentará fazer a chamada:

resultado = servidor.calcular_pontos(120, 2), Mas não conseguirá se conectar ao servidor em localhost:8004.


