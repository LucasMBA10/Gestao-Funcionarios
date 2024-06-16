from locust import HttpUser, task, between

class UserBehavior(HttpUser):
    wait_time = between(0.5, 1)  # Tempo de espera entre as requisições
    host = "http://localhost:8000"  # Definindo o host base para as requisições

    @task
    def create_employee(self):
        headers = {'Content-Type': 'application/json'}
        payload = {
            "cpf": "12345678901",
            "name": "Usuário Teste",
            "position": "Desenvolvedor",
            "salary": 5000,
            "created_at": "2024-06-16T12:00:00Z",
            "updated_at": "2024-06-16T12:00:00Z"
        }
        response = self.client.post("/employee", json=payload, headers=headers)
        if response.status_code != 200:
            print(f"Erro ao criar usuário. Status code: {response.status_code}")

    @task
    def list_all_employees(self):
        response = self.client.get("/employees")
        if response.status_code != 200:
            print(f"Erro ao listar usuários. Status code: {response.status_code}")
