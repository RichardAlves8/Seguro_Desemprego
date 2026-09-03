# Simulador de Seguro-Desemprego
 
Programa em Python feito para a disciplina de Ciência da Computação (2º semestre - UNIP), que simula a verificação de direito ao benefício do Seguro-Desemprego com base nas regras da legislação brasileira.
 
## O que o programa faz
 
O usuário responde a um questionário interativo no terminal, informando sua situação profissional. O programa então:
 
1. Verifica se o usuário se enquadra em um dos três critérios de elegibilidade:
   - Trabalhador formal (demitido sem justa causa ou afastado para qualificação profissional);
   - Pescador profissional artesanal (Seguro-Defeso);
   - Trabalhador resgatado de regime de trabalho forçado.
2. Verifica se as condições específicas de cada critério são atendidas (tempo trabalhado, número de solicitações anteriores, motivo do desligamento, etc).
3. Caso tenha direito ao benefício, calcula o valor da parcela com base na média salarial dos últimos três meses.
4. Calcula o número de parcelas a que o usuário tem direito.
 
O programa vai pedir as informações necessárias diretamente no terminal, conforme a situação escolhida.
 
## Critérios considerados
 
- Tempo mínimo de trabalho para ter direito ao benefício.
- Número de vezes que o benefício já foi solicitado (a regra de tempo mínimo muda a cada nova solicitação).
- Faixas de cálculo do valor da parcela, respeitando o piso do salário mínimo.
- Regras específicas para estudantes (Bolsa Qualificação) e para pescadores artesanais.
## Observação
 
Este é um simulador para fins educacionais. Os valores e regras usados são baseados na legislação vigente na época do desenvolvimento, mas não substituem uma consulta oficial ao site gov.br ou a um profissional especializado.
