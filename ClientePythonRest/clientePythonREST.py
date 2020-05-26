from suds.client import Client
print((Client("http://localhost:8080/ValidadorCpfRest/cpf?word=cpf")).service.CPF())
