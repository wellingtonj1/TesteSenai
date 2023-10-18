frutas = ["maça", "pera", "pessego"]
frutas.insert(0, "Outra fruta")
frutas.append('dado')
frutas[4] = "Manga"
print(frutas)
posicao = 0
while posicao < len(frutas):
    frutas[posicao] = frutas[posicao] + "ss"
    posicao+=1
print(frutas)
