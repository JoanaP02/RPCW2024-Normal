# Ontologia da História do Sr. João

## Classes

1. **Pessoa**
2. **Fazenda**
3. **Animal**
4. **Fruta**
5. **Vegetal**
6. **Produto**
7. **Trator**
8. **Cachorro**
9. **Feira**
10. **TrabalhadorTemporario**

## Atributos de cada Classe (Data Properties)

1. **Pessoa**
   - nome (string)
   - função (string)

2. **Fazenda**
   - nome (string)
   - tamanho (float)

3. **Animal**
   - tipo (string)
   - nome (string)
   - quantidade (int)

4. **Fruta**
   - tipo (string)
   - quantidade (int)

5. **Vegetal**
   - tipo (string)
   - quantidade (int)

6. **Produto**
   - tipo (string)
   - quantidade (int)

7. **Trator**
   - marca (string)
   - modelo (string)

8. **Cachorro**
   - nome (string)

9. **Feira**
   - nome (string)
   - dia (string)

10. **TrabalhadorTemporario**
    - nome (string)
    - horasTrabalhadas (int)
    - salarioPorHora (float)

## Relações (Object Properties)

1. **Pessoa**
   - temFazenda (range: Fazenda)
   - cultivaFruta (range: Fruta)
    - cultivaFruta (range: Fruta)
    - cultivaVegetal (range: Vegetal)

   - criaAnimais (range: Animal)
   - trocaProdutosCom (range: Pessoa)
   - vendeNaFeira (range: Feira)
   - fazProduto (range: Produto)

2. **Fazenda**
   - temAnimal (range: Animal)
   - temTrator (range: Trator)
   - temCachorro (range: Cachorro)
   - contrataTrabalhador (range: TrabalhadorTemporario)

3. **Animal**
   - éProtegidoPor (range: Cachorro)

4. **TrabalhadorTemporario**
   - trabalhaEm (range: Fazenda)

## Indivíduos com Atributos e Relações

1. **SrJoao (Pessoa)**
   - nome: "João"
   - função: "agricultor"
   - temFazenda: FazendaSaoJose

2. **SraMaria (Pessoa)**
   - nome: "Maria"
   - função: "ajudante"

3. **Pedro (Pessoa)**
   - nome: "Pedro"
   - função: "ajudante"

4. **Ana (Pessoa)**
   - nome: "Ana"
   - função: "ajudante"

5. **SrCarlos (Pessoa)**
   - nome: "Carlos"
   - função: "agricultor"
   - temFazenda: FazendaCarlos

6. **FazendaSaoJose (Fazenda)**
   - nome: "São José"
   - temAnimal: [Vacas, Galinhas, Porcos]
   - cultivaFruta: [Macas, Laranjas, Bananas]
   - temTrator: TratorSaoJose
   - temCachorro: Rex

7. **Vacas (Animal)**
   - tipo: "vaca"
   - quantidade: 3

8. **Galinhas (Animal)**
   - tipo: "galinha"
   - quantidade: 10

9. **Porcos (Animal)**
   - tipo: "porco"
   - quantidade: 5

10. **Macas (Fruta)**
    - tipo: "maçã"
    - quantidade: 100

11. **Laranjas (Fruta)**
    - tipo: "laranja"
    - quantidade: 150

12. **Bananas (Fruta)**
    - tipo: "banana"
    - quantidade: 200

13. **TratorSaoJose (Trator)**
    - marca: "John Deere"
    - modelo: "X123"

14. **Rex (Cachorro)**
    - nome: "Rex"

15. **FazendaCarlos (Fazenda)**
    - nome: "Fazenda do Carlos"
    - cultivaVegetal: [Tomates, Alfaces, Cenouras]

16. **Tomates (Vegetal)**
    - tipo: "tomate"
    - quantidade: 300

17. **Alfaces (Vegetal)**
    - tipo: "alface"
    - quantidade: 200

18. **Cenouras (Vegetal)**
    - tipo: "cenoura"
    - quantidade: 250

19. **FeiraSaoJose (Feira)**
    - nome: "Feira de São José"
    - dia: "sábado"

20. **Trabalhador1 (TrabalhadorTemporario)**
    - nome: "José"
    - horasTrabalhadas: 8
    - salarioPorHora: 10.0
    - trabalhaEm: FazendaSaoJose
