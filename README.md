<h1 align="center">ClimaTempy</h1>
O intuito de criar essa Lib, é ajudar os Dev's na hora de criar algum projeto, que necessita de uma informação sobre o clima tempo do local especifico.
<br>

---
## De onde vem os dados ?
Como fonte de dados, usei de base o site <https://www.climatempo.com.br>, o qual verifiquei algumas mudanças na estrutura de requisições do site nos ultimos meses, podendo ser instável algumas vezes a Lib.\
Vale ressaltar aqui que todos os parâmetros retornados do site irão vir em inglês.

---
## Como usar ?
```python
from climatempy import ClimaTempo

c = ClimaTempo("sua cidade")
print(c.dados) # Todos os dados da resposta do site fonte
print(c.clima) # Um dicionário com todas as informações
```
Resultado
```python
# Dados
{'idlocale': 6910, 'idcity': 179, 'capital': False, 'idcountry': 7, 'ac': 'BR', 'country': 'Brasil', 'uf': 'MG', 'city': 'Ponte Nova', 'region': 'SE', 'seaside': False, 'latitude': -20.416, 'longitude': -42.909, 'tourist': False, 'agricultural': False, 'base': 'cities', 'searchPoints': 200}

# Clima
{'temperature': 26, 'condition': 'Poucas nuvens', 'humidity': 83, 'sensation': 28, 'windVelocity': 18, 'pressure': 1023, 'date': '2022-09-04 18:50:24'}
```