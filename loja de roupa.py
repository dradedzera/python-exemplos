#Formatação de Strings com várias linhas
escola = "Senai"
curso = "Desenvolvimento de Sistemas"
uc = "Lógica de Programação"
matricula = 34
nota = 8.999999
print(f"Escola: {escola}\n"
      f"Curso: {curso}\n"
      f"Unidade Curricular: {uc}"
      f"Mátricula: {matricula:06d}"
      f"Nota: {nota:.2f}")
