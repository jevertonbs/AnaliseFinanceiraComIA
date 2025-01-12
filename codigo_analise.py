import matplotlib.pyplot as plt

# Renaming columns for better handling
df.columns = ['Date', 'Type', 'Category', 'Description', 'Value', 'Payment Method', 'Status']

# Convert Value to numeric if necessary and Date to datetime
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Calculate total entries and exits
total_entradas = df.loc[df['Type'] == 'ENTRADA', 'Value'].sum()
total_saidas = df.loc[df['Type'] == 'SAÍDA', 'Value'].sum()
saldo = total_entradas - total_saidas

# Summarize spending by category
spending_by_category = df[df['Type'] == 'SAÍDA'].groupby('Category')['Value'].sum().sort_values(ascending=False)

# Monthly summary
df['Month'] = df['Date'].dt.to_period('M')
monthly_summary = df.groupby(['Month', 'Type'])['Value'].sum().unstack().fillna(0)

# Identify pending transactions
pending_transactions = df[df['Status'] == 'Pendente']

# Plotting spending by category
plt.figure(figsize=(10, 6))
spending_by_category.plot(kind='bar', color='coral')
plt.title('Gastos por Categoria')
plt.ylabel('Valor')
plt.xlabel('Categoria')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('mntdatagastos_por_categoria.png')

# Plotting monthly cash flow
plt.figure(figsize=(10, 6))
monthly_summary.plot(kind='bar', stacked=True)
plt.title('Fluxo de Caixa Mensal')
plt.ylabel('Valor')
plt.xlabel('Mês')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('mntdatafluxo_de_caixa_mensal.png')

# Outputs for review
total_entradas, total_saidas, saldo, spending_by_category, pending_transactions, monthly_summary.tail()
