import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega os dados
df = pd.read_csv("vendas.csv")

# Calcula receita
df["receita"] = df["quantidade"]*df["preco_unitario"]

# Total vendido por produto
vendas_por_produto = df.groupby("produto")["receita"].sum().sort_values(ascending=False)


# Gráfico 1 - Vendas por produto
plt.figure(figsize=(8,4))
sns.barplot(x=vendas_por_produto.index, y=vendas_por_produto.values)
plt.title("Receita por Produto")
plt.ylabel("Receita (R$)")
plt.xlabel("Produto")
plt.tight_layout()
plt.show()

# Gráfico 2 - Vendas por vendedor
plt.figure(figsize=(8,4))
sns.barplot(x=vendas_por_vendedor.index, y=vendas_por_vendedor.values, palette="viridis")
plt.title("Receita por Vendedor")
plt.ylabel("Receita (R$)")
plt.xlabel("Vendedor")
plt.tight_layout()
plt.show()
