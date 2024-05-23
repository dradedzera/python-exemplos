import random
alunos=["Gustavo", "Maria", "Pedro", "Ana", "Mariana"]
print(f"Lista: {alunos}")
# Embaralhar a Lista
random.shuffle(alunos)
print(f"Lista Embaralhada: {alunos}")
# Escolhe um aluno aleatoriamente
aluno_sorteado = random.choice(alunos)
print(f"Aluno sorteado: {aluno_sorteado}")
# Ordena a lista Decrescente
alunos.sort(reverse=True)
print(f"Lista decrescente: {alunos}")