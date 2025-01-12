# Relatório Financeiro

Este repositório contém um relatório financeiro gerado a partir de uma base de dados fornecida, com análises e visualizações detalhadas. O objetivo é fornecer insights sobre entradas e saídas financeiras, além de identificar tendências e áreas de melhoria.

## Funcionalidades

- **Resumo Financeiro Geral:**
  - Total de entradas, saídas e saldo atual.
  
- **Análises por Categoria:**
  - Identificação das categorias com maiores gastos.

- **Fluxo de Caixa Mensal:**
  - Evolução de entradas e saídas ao longo dos meses.

- **Transações Pendentes:**
  - Lista de transações que ainda não foram quitadas.

- **Gráficos:**
  - Visualizações de gastos por categoria e fluxo de caixa mensal.

## Estrutura do Repositório

- `data/` - Diretório contendo a base de dados utilizada no relatório.
- `scripts/` - Scripts em Python usados para gerar as análises e gráficos.
- `output/` - Relatórios e gráficos gerados, incluindo o PDF final.

## Requisitos

- Python 3.8 ou superior
- Bibliotecas necessárias:
  - `pandas`
  - `matplotlib`
  - `fpdf`

Para instalar as dependências, execute:
```bash
pip install -r requirements.txt
```

## Uso

1. Coloque os dados financeiros no diretório `data/`.
2. Execute o script principal para gerar as análises e gráficos:
```bash
python scripts/financial_report.py
```
3. O relatório em PDF será salvo no diretório `output/`.

## Exemplos de Saída

### Gráficos

- **Gastos por Categoria:**
![Gastos por Categoria](output/gastos_por_categoria.png)

- **Fluxo de Caixa Mensal:**
![Fluxo de Caixa Mensal](output/fluxo_de_caixa_mensal.png)

### PDF

O relatório em PDF pode ser encontrado em `output/Relatorio_Financeiro.pdf`.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT.
