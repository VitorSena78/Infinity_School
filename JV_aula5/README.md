range() em Python são start, stop e step

Exemplos:
    range(5): Gera 0, 1, 2, 3, 4 (começa em 0, vai até 5, pulo de 1).
    range(2, 8): Gera 2, 3, 4, 5, 6, 7 (começa em 2, vai até 8, pulo de 1).
    range(1, 10, 2): Gera 1, 3, 5, 7, 9 (começa em 1, vai até 10, pulo de 2).
    range(10, 0, -1): Gera 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 (decrescente). 


# Formas de criar listas vazias em python:

A forma mais comum e correta de declarar uma lista vazia em **Python** é:

```python
lista = []
```

### Comentários rápidos:

* `[]` cria uma nova lista vazia.
* Você pode adicionar elementos depois usando `append()`, `extend()` ou outras operações.
* Também é possível usar `list()`, mas `[]` é mais simples e mais rápido.

### Exemplos de uso:

```python
# Criando uma lista vazia
lista = []

# Adicionando elementos
lista.append(10)
lista.append("Python")
lista.append(True)

print(lista)  # Resultado: [10, 'Python', True]
```



# Listas

---

# ✅ **O que são listas em Python?**

**Listas** são estruturas que armazenam vários valores em uma única variável.
Elas são **mutáveis**, ou seja, você pode alterar, adicionar ou remover elementos depois de criadas.

Exemplo:

```python
frutas = ["maçã", "banana", "uva"]
```

---

# ✅ **Fatiamento de listas – `lista[início:fim:passo]`**

O fatiamento permite pegar partes da lista sem alterar a original.

### 📌 **Significado de cada argumento:**

### **1. início**

* Índice onde o fatiamento começa (inclusivo).
* Se não for informado, começa no início da lista.

### **2. fim**

* Índice onde o fatiamento termina (**exclusivo**, ou seja, não inclui esse índice).
* Se não informado, vai até o final da lista.

### **3. passo**

* Indica de quantos em quantos elementos a fatia vai andar.
* O padrão é `1`.
* Pode ser negativo para inverter a ordem.

---

# ✅ **Exemplos práticos**

### ✔ **Usando início e fim**

```python
lista = [0, 1, 2, 3, 4, 5]

print(lista[1:4])  # [1, 2, 3]
```

* Começa no índice **1**
* Vai até o índice **4**, mas **não inclui** o 4

---

### ✔ **Omitindo início**

```python
print(lista[:3])  # [0, 1, 2]
```

---

### ✔ **Omitindo fim**

```python
print(lista[2:])  # [2, 3, 4, 5]
```

---

### ✔ **Usando passo**

```python
print(lista[0:6:2])  # [0, 2, 4]
```

---

### ✔ **Passo negativo (invertendo a lista)**

```python
print(lista[::-1])  # [5, 4, 3, 2, 1, 0]
```

---

### ✔ **Pegando elementos de 2 em 2**

```python
print(lista[::2])  # [0, 2, 4]
```

---

# ✔ Resumo rápido

| Notação         | Significado                 |
| --------------- | --------------------------- |
| `a[:]`          | copia a lista inteira       |
| `a[início:]`    | da posição início até o fim |
| `a[:fim]`       | do início até fim-1         |
| `a[início:fim]` | pega uma parte específica   |
| `a[::passo]`    | pula elementos              |
| `a[::-1]`       | lista invertida             |

---
