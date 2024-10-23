import sqlite3

class Plantao:
    def conexao(self):

        # Conecta ao banco de dados
        conexao = sqlite3.connect("plantao_db")

        # Acessar o objeto cursor() da biblioteca sqlite3, para manipular dados do banco
        consulta = conexao.cursor()

        # Verificar se a tabela existe ou não
        tabela = """
        CREATE TABLE IF NOT EXISTS plantoes(
            id_medico INTEGER PRIMARY KEY,
            nome_medico VARCHAR(100),
            especialidade VARCHAR(100),
            data DATE,
            turno VARCHAR(100)
        );
        """
        # Executar o comando de criação da tabela
        consulta.execute(tabela)
        return conexao
    
    def cadastrar(self, id_medico, nome_medico, especialidade, data, turno):

        conexao = self.conexao()

        # Criando comando SQL para inserir os dados na tabela
        sql = "INSERT INTO plantoes (id_medico, nome_medico, especialidade, data, turno) VALUES (?, ?, ?, ?, ?)" # ? no lugar dos dados reais, para evitar possíveis ataques de sql injection. Isso é uma implementação da biblioteca sqlite3.

        campos = (id_medico, nome_medico, especialidade, data, turno) # Criando uma tupla com os dados que irão substituir ?

        consulta = conexao.cursor()

        consulta.execute(sql, campos) # Executar o comando sql e substituir '?' pelos campos

        conexao.commit() # Gravar os dados no banco

        print(consulta.rowcount, "linha(s) inserida(s) com sucesso")

        print("-" * 40)

        conexao.close() # Encerrar a conexão

    def consultar(self):
        conexao = sqlite3.connect("plantao_db")

        consulta = conexao.cursor() # Acessar o objeto cursor() da biblioteca sqlite3, para manipular dados do banco

        sql = "SELECT * FROM plantoes" # Criando comando SQL para inserir os dados na tabela

        consulta.execute(sql) # Executar o comando sql

        resultado = consulta.fetchall() #fetchall() irá trazer todos os registros que existem na tabela do banco de dados

        for itens in resultado:
            print(f"ID: {itens[0]}")
            print(f"Nome: {itens[1]}")
            print(f"Especialidade: {itens[2]}")
            print(f"Data: {itens[3]}")
            print(f"Turno: {itens[4]}")
            print("-" * 40) 
        
        conexao.close()
    
    def consultar_individual(self, id_medico):

        conexao = sqlite3.connect("plantao_db") # Conexão com o banco de dados

        consulta = conexao.cursor() # Acessar o objeto cursor() da biblioteca sqlite3, para manipular dados do banco

        sql = "SELECT * FROM plantoes WHERE id_medico = ?" # Criando comando SQL para inserir os dados na tabela

        consulta.execute(sql, (id_medico,))

        resultado = consulta.fetchall()

        if resultado:
            print(f"ID: {resultado[0]}")
            print(f"Nome: {resultado[1]}")
            print(f"Especialidade: {resultado[2]}")
            print(f"Data: {resultado[3]}")
            print(f"Turno: {resultado[4]}")
        else:
            print("Nenhum plantão encontrado com esse ID.")
            print("-" * 40)

        conexao.close()

    def atualizar(self, id_medico, novo_nome_medico):

        conexao = sqlite3.connect("plantao_db") # Estabelecendo a conexão

        sql = "UPDATE plantoes SET nome_medico = ? WHERE id_medico = ?"

        campos = (novo_nome_medico, id_medico)

        consulta = conexao.cursor()

        consulta.execute(sql, campos)

        conexao.commit()

        print(consulta.rowcount, "linha(s) atualizada(s) com sucesso")

        print("-" * 40)

        conexao.close()

    def deletar(self, id_medico):

        conexao = sqlite3.connect("plantao_db") # Estabelecendo a conexão

        sql = "DELETE FROM plantoes WHERE id_medico = ?"

        campos = (id_medico,) #É preciso a vírgula depois do item para configurar que temos uma tupla, caso contrário não será aceito como uma tupla válida.

        consulta = conexao.cursor()

        consulta.execute(sql, campos)

        conexao.commit()

        print(consulta.rowcount, "linha(s) deletada(s) com sucesso")

        print("-" * 40)

        conexao.close()
