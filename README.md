
# Sistema de Monitoramento Blue Ocean

## Integrantes
- Gabriel Gouvea - RM555528
- Miguel Kapicius - RM556198
- Thiago Ferreira - RM555608

---

## Descrição do Projeto

O projeto Blue Ocean visa criar uma plataforma integrada para monitoramento da qualidade da água, tanto no mar aberto quanto em costas de comunidades riberinhas ou outras dependentes da pescas. Utilizando sensores conectados a placas Arduino, o sistema mede parâmetros críticos como temperatura, pH, salinidade e níveis de poluição. Os dados são coletados, processados, armazenados e apresentados em uma interface web de fácil utilização.

### Objetivos
- Monitoramento contínuo e em tempo real da qualidade da água.
- Facilitar a identificação rápida de problemas e implementação de medidas corretivas.
- Promover a sustentabilidade dos ecossistemas aquáticos.
- Fornecer informações relevantes para a população local e pesquisadores.

---

## Instruções de Uso

### Requisitos
- Python 3.x
- Bibliotecas Python: `matplotlib`, `os`

### Instalação das Dependências
1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale as bibliotecas necessárias utilizando o pip:
   ```bash
   pip install matplotlib
   ```

### Executando o Programa
1. Clone o repositório do projeto ou baixe o código fonte.
2. Navegue até o diretório onde o código está localizado.
3. Execute o programa:
   ```bash
   python main.py
   ```

### Funcionalidades

#### Gerar Análise Detalhada
1. Ao iniciar o programa, digite `gerar` para começar a análise detalhada.
2. Escolha o tipo de dado para inserir (`ph`, `temperatura`, `nível do mar`) ou `sair` para finalizar.
3. Insira o número de dias para coleta de dados.
4. Digite os valores para cada dia.
5. O programa irá plotar os dados em um gráfico e mostrar a média dos valores inseridos.

#### Consultar Valor
1. Ao iniciar o programa, digite qualquer tecla exceto `gerar` para consultar um valor específico.
2. Escolha o tipo de valor que quer consultar (`ph` ou `temperatura`).
3. Insira o valor coletado.
4. O programa fornecerá uma análise do valor inserido, comparando-o com os padrões normais.

#### Encerrar ou Continuar
1. Após a execução de uma funcionalidade, digite `N` para encerrar o programa ou qualquer outra tecla para realizar mais uma verificação.

---

## Detalhes Técnicos

### Estrutura do Código

- **Dicionário para Temperatura**: Contém as faixas de temperatura normal para diferentes regiões do Brasil.
- **Função `clear()`**: Limpa o terminal.
- **Função `check_number(prompt)`**: Verifica se a entrada é um número.
- **Função `collect_data(data_type)`**: Coleta dados do usuário para o tipo especificado.
- **Função `calculate_average(data)`**: Calcula a média dos valores.
- **Função `plot_data(data, data_type)`**: Plota os dados coletados em um gráfico.
- **Função `check_region(prompt)`**: Verifica a região inserida pelo usuário.
- **Função `consult(data_type)`**: Consulta o valor inserido e fornece uma análise.
- **Função `main()`**: Menu principal do programa, gerencia a execução e navegação entre funcionalidades.

---

## Contribuições Futuras
- Integração com sensores reais utilizando placas Arduino.
- Implementação de funcionalidades adicionais, como monitoramento de salinidade e níveis de poluição.
- Desenvolvimento de uma interface web para visualização de dados em tempo real.

---

