# Vincenzo Amendola 
# Lucas Matos

### Nome do(a) Aluno(a)
Profº.: André Cassulino

## Escopo 1

## Gestão de Funcionários
Este projeto visa criar um sistema de gestão de funcionários para facilitar o registro, atualização e consulta das informações dos colaboradores de uma empresa. O sistema permite gerenciar funcionários, associá-los a departamentos específicos e atribuir cargos dentro desses departamentos.

## Funcionalidades Principais
Cadastro de Funcionários:

Registra informações como CPF, nome, salário, data de admissão, departamento e cargo.
Gerenciamento de Departamentos:

Permite cadastrar e gerenciar os diferentes departamentos da empresa.
Cadastro de Cargos:

Registra os cargos disponíveis na empresa com nome e descrição.
Associação Funcional:

Associa cada funcionário a um departamento e a um cargo específico dentro desse departamento.
Consulta e Atualização:

Permite consultar e visualizar informações detalhadas dos funcionários, além de atualizar dados como salário, departamento ou cargo.
Benefícios

Organização Eficiente: Facilita a organização dos funcionários por departamento e cargo.
Acesso Rápido às Informações: Permite acesso rápido e fácil às informações dos colaboradores.
Tomada de Decisão Baseada em Dados: Fornece dados atualizados para auxiliar na tomada de decisões estratégicas de gestão de pessoal.

### Ferramentas Escolhidas (Algumas em fase de teste)
- **Python**: Linguagem de programação.
- **FrameWork Python**: Django ou FastApi.
- **Locust ou K6**: Ferramentas de teste de carga e desempenho.
- **ORM e Configurações de Banco de Dados**: Pymongo, Pydantic, PostgreSQL, MongoDB, redis.
- **React e Vite**: Utilizando TypeScript ou HTML/CSS/SASS.
- **Ambiente de Desenvolvimento ou Deploy (Containerização)**: Docker ou Podman (pods).

### Função de Cada Integrante
- **Lucas Matos (DevOps, Dev Python)**: Responsável pela containerização, gestão de Gitflow, e implementação de padrões de projetos.
- **Vincenzo Amendola (Dev Python, Data Science, PO)**: Desenvolvimento em Python, testes, e observabilidade.

### Gestão do Projeto
- **GitHub**: Git para versionamento de commits, usando o padrão gitflow com padrões de branches, develop, feature, master, main.

## Gestão de Funcionários

Este projeto visa criar um sistema de gestão de funcionários para facilitar o registro, atualização e consulta das informações dos colaboradores de uma empresa. O sistema permite gerenciar funcionários, associá-los a departamentos específicos e atribuir cargos dentro desses departamentos.

### Como Usar

#### Docker

Para rodar o projeto utilizando Docker, siga os passos abaixo:

```
# Clone o Repositório
git clone https://github.com/LucasMBA10/Gestao-Funcionarios.git
```
```
cd project
```
```
# Construa e Execute os Containers
docker-compose up --build
```
```
## teste de request
locust -f locustfile.py --headless -u 50 -r 10 --host http://localhost:8000 --run-time 1m

```

### Estrutura de banco de dados (versão beta)

![alt text](image.png)