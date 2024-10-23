'''
SENAI – CEPT RAIMUNDO TEIXEIRA
Alunos: Kayron Mendes, Ludmylla Melo, Luize Pinheiro e Giovanna Fonseca
Instrutor: Anderson Bruno

Relatório do Projeto – Gerenciamento de plantão de médicos


O trabalho proposto ao grupo tinha como tema Gerenciamento de plantão de médicos, foi utilizada a linguagem de programação Python. Nos últimos anos, o Python emergiu como uma das linguagens de programação mais renomadas globalmente. Isso se deve, principalmente, à sua versatilidade: ele é utilizado em aprendizado de máquina, desenvolvimento de websites e até na automação de tarefas e testes de software. Ademais, sua semelhança com a linguagem natural atrai muitos usuários, incluindo tanto desenvolvedores quanto profissionais que atuam nesse setor. 
Quem está escrevendo o relatório é Kayron Mendes, que ficou responsável pela escrita do relatório geral e a revisão final dos códigos. Durante o processo os membros Luize e Giovanna encarregaram-se de: Cadastrar, Deletar, Consultar e Plantão.
Sendo que em Cadastrar o código gerencia informações sobre médicos em um banco de dados SQLite. Ele cria uma tabela para armazenar dados como ID, nome, especialidade, data e turno. Depois, solicita que o usuário insira informações de um médico, prepara e executa a inserção desses dados, confirmando a operação e informando quantas linhas foram adicionadas. Assim, facilita o registro de plantões médicos.
 
Em Deletar o código gerencia um banco de dados SQLite para deletar registros de médicos plantonistas. Ele se conecta a um banco de dados, cria uma tabela se necessário e solicita ao usuário o ID de um médico para remover. Após executar o comando de exclusão e confirmar as alterações, informa quantas linhas foram deletadas e encerra a conexão com o banco.

Já em Consultar o código gerencia um banco de dados SQLite para consultar e exibir informações sobre médicos plantonistas. Ele se conecta ao banco, cria uma tabela para armazenar dados dos médicos, se necessário, e executa um comando para selecionar todos os registros. Os dados são exibidos, mostrando o ID e o nome de cada médico, antes de encerrar a conexão com o banco.

E em Plantão é definida uma classe chamada "Plantão" para gerenciar informações sobre médicos em plantões usando um banco de dados SQLite. 

A classe possui três métodos principais:
1.Conexão: Estabelece conexão com o banco de dados e cria uma tabela para armazenar dados dos médicos, se necessário.
2.Cadastro: Permite registrar informações de um médico, como ID, nome, especialidade, data e turno, inserindo esses dados na tabela.
3.Consulta: Recupera e exibe todos os registros da tabela, mostrando detalhes de cada médico.
A conexão com o banco de dados é fechada após cada operação, garantindo a liberação dos recursos. Assim, a classe organiza e facilita a gestão dos dados dos plantões médicos.

A integrante Ludmylla ficou responsável por: Atualizar e Consultar Plantão Individual. Além de adicionar ao código MENU.
O atualizar é responsável pela função que atualiza informações de um plantão no banco de dados. Ela recebe um objeto de plantão, um ID e novos valores opcionais para o nome do médico, especialidade, data e turno. Se houver informações a atualizar, ela executa um comando SQL para modificar o registro correspondente e confirma as mudanças. Se não houver dados para atualizar, exibe uma mensagem informando isso.

O Consultar plantão individual função consulta um plantão específico no banco de dados, recebendo um ID como parâmetro. Ela executa um comando SQL para buscar os dados correspondentes e, se encontrar um registro, exibe as informações. Se não houver registro, uma mensagem informa que o plantão não foi encontrado.

O MENU é um código que cria um menu interativo para gerenciar plantões de médicos, permitindo cadastrar, consultar, deletar e atualizar informações sobre plantões, além de consultar um plantão específico. O menu continua a exibir opções até que o usuário decida sair, facilitando a interação com os dados e encerrando a conexão com o banco de dados ao final.'''