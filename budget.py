import math

class Category:
    """
    Classe Category possui os métodos: deposit, withdraw, get_balance, transfer e check_funds.
    Esta classe é capaz de instaciar objetos de diferentes bases de categorias diferentes.
    
    Método deposit:
     - deposit (amount : int, description : str = "") -> None
     Um método deposit que aceita um valor e uma descrição. Se nenhuma descrição for fornecida, 
     o padrão deve ser uma string vazia. O método deve anexar um objeto à lista de razão na 
     forma de {"amount": amount, "description": description}.
     
    Método withdraw:
     - withdraw (amount : int, description : str = "") -> Bool
     Um método withdraw que é semelhante ao método deposit, mas o valor passado deve ser 
     armazenado no livro-razão como um número negativo. Se não houver fundos suficientes, 
     nada deve ser adicionado ao livro-razão. Este método deve retornar True se a retirada 
     ocorreu, e False caso contrário.
     
    Método get_balance:
     - get_balance () -> float
     Um método get_balance que retorna o saldo atual da categoria de orçamento com base nos 
     depósitos e saques ocorridos.
     
    Método transfer:
     - transfer (amount : int, category : object) -> bool
     Um método de transfer que aceita um valor e outra categoria de orçamento como argumentos. 
     O método deve adicionar um saque com o valor e a descrição "Transferência para 
     [Categoria de Orçamento de Destino]". O método deve então adicionar um depósito à outra 
     categoria de orçamento com o valor e a descrição "Transferência de 
     [Categoria de orçamento de origem]". Se não houver fundos suficientes, nada deve ser 
     adicionado a nenhum dos livros. Este método deve retornar True se a transferência ocorreu, 
     e False caso contrário.
     
    Método check_funds:
     - check_funds (amount) -> bool
     Um método check_funds que aceita um valor como argumento. Ele retorna "Falso" se o 
     valor for maior que o saldo da categoria de orçamento e retorna "Verdadeiro" 
     caso contrário. Este método deve ser usado tanto pelo método withdraw quanto pelo 
     método transfer.
    """
    def __init__(self,name) -> None:
        self.name = name
        self.ledger = []
        self.money_spent = 0
        
    def __str__(self) -> str:
        head = f"{self.name:*^30}" + "\n"
        body = ""
        footer = f"Total: {self.get_balance()}"
        
        for item in self.ledger:
            body += f"{item['description'][:23]:<23}" + f"{item['amount']:>7.2f}" + "\n"
        
        return head+body+footer
    
    
    def deposit (self, amount, description = "") -> None:
        self.ledger.append(
            {
                "amount":amount,
                "description":description
            }
        )
        
        
    def withdraw (self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append(
                {
                    "amount":-amount,
                    "description":description
                }
            )
            self.money_spent += amount
            return True
        
        else:
            return False
    
    
    def get_balance (self):
        return sum([ i["amount"] for i in self.ledger])
        
        
    def transfer (self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount,f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
        
        
    def check_funds (self, amount):
        return False if (amount > self.get_balance()) else True
        
#Dividir para conquistar! 
#Dividi em header, body e footer para plotar o grafico 
def create_spend_chart(categories):
    #Carregando as variaveis 
    header = "Percentage spent by category\n"
    body = ""
    lines = ""
    footer = ""
    
    #Obtento uma lista com os valores gastos, obtento o total e calculando os valores para plotar no grafico
    list_values = [categorie.money_spent for categorie in categories ]
    total = sum(list_values)
    values_percents = [math.floor((item / total) * 100) for item in list_values]
    
    #Criando o body do grafico onde contém a porcentagem dos gastos
    for row in range(100, -1, -10):
        body += f"{row:>3}" + "|"
        for percent in values_percents:
            body += " o " if percent >= row else "   "
            
        body += " \n"
    
    #As linhas que separam a parte body e footer do grafico          
    lines += "    " + f"{lines:-^{len(values_percents)*3}}" + "-\n"
    
    #Obtento qual é o maior nome das categorias para adicionar um " " espaço em branco para que todos os nomes tenham o mesmo tamanho
    length_max = max([len(categorie.name) for categorie in categories])
    list_names = [f"{categorie.name:<{length_max}}" for categorie in categories]
    
    #Criando o footer. Para cada linha de cada nome é criado simultaneamente. Poderia ter usado mais um loop para realizar a mesma função, mas ao final de cada row teria que usar uma "\n" para quebrar uma nova linha.
    for row in range(length_max):
        footer += "    " + f"{list_names[0][row]:^3}" + f"{list_names[1][row]:^3}" + f"{list_names[2][row]:^3}" + " \n"
    
    #Realizando a junção do header,body,lines e footer numa string para conseguir ver o retorno no ipdb      
    str_return = header + body + lines + footer[:-1]
    
    #import ipdb;ipdb.set_trace() isso me ajuda muito xD 
    return str_return