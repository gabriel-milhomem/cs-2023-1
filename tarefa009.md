# Tarefa Individual 009 - 15/05/2023

1. Considere as seguintes referências utilizadas nas aulas do dia 15/05/2023:
   1. [Fatores de qualidade na programação.](https://www.devmedia.com.br/fatores-de-qualidade-na-programacao/29780)
   2. [Qualidade do código e sua importância para um desenvolvimento bem sucedido.](https://bring.com.br/blog/2019/09/10/qualidade-do-codigo-e-sua-importancia-para-um-desenvolvimento-bem-sucedido/)
   3. [Porque a qualidade de código é importante?](https://ezdevs.com.br/porque-a-qualidade-de-codigo-e-importante/)
   4. [Princípios para produzir um código bonito.](https://www.profissionaisti.com.br/principios-para-produzir-um-codigo-bonito/)
   5. [6 dicas fundamentais para um código de qualidade.](https://www.youtube.com/watch?v=MMAu_1KMcMA)
   6. [6 Questões para a Qualidade do Código.](https://vizir.com.br/2016/09/6-questoes-para-a-qualidade-do-codigo-ruby-conf-br-4/)
   7. [DevQA: Como medir qualidade de código?](https://kamillaqueiroz.medium.com/devqa-como-medir-qualidade-de-código-6149fada1e)
   8. [Como melhorar o gerenciamento do código fonte?](https://gaea.com.br/como-melhorar-o-gerenciamento-de-codigo-fonte/)

2. Elaborar um texto sobre um deles, destacando:
    1. A ideias principais do texto;
    2. O que é novidade para você, em relação ao conteúdo do artigo;
    3. O que já era conhecido por você.
3. Escrever um parágrafo com suas palavras comentando o conteúdo do artigo.

## Texto: 6 Dicas fundamentais para um código de qualidade.

### Ideias principais

- **Princípio dos 4 Olhos:** Além do programador que programou o código, mais duas pessoas (4 olhos) devem fazer a revisão do código. O método mais utilizado para fazer o Code Review é pelo método de Pull Request feito pelo Git. Durante a revisão do código, deve ser verificado a legibilidade e manutenabilidade do código, garantir se o código contempla todos os casos de usos e regras de negócio, se possui testes e se estão testando da forma correta, além de tratar os casos de exceções.
- **Integração Continua:** É uma prática de desenvolvimento de software em que os membros da equipe integram o seu código com frequência (quase diariamante) para a MAIN. Cada integração é verificado por um build automatizado que inclui testes automatizados para detectar erros os mais rápidos possíveis. A vantagem dessa prática é o rápido feedback para o desenvolvedor e a garantia que esta sempre desenvolvendo em um ambiente estável.
- **Convenções no Código:** Ter um conjunto de convenções de codificação que todos os membros da equipe seguem. Isso inclui regras para declaração de variáveis, convenções de nomenclatura, entre outros. O uso de um linter pode ajudar a garantir que as convenções sejam seguidas e aumentar a legibilidade e a manutenibilidade do código
- **Testes:** Realizar testes de forma abrangente para filtrar bugs críticos e garantir que o código funcione como esperado. Isso inclui testes unitários, testes de integração e testes de regressão. Priorizar os testes unitários e utilizar ferramentas de testes apropriadas.
- **Analisar Bugs:** Analisar os bugs que ocorrem, avaliar seu impacto e aprender com eles. Identificar as causas raiz dos bugs, revisar a estratégia de testes e buscar formas de prevenção para evitar que ocorram novamente. Utilizar ferramentas de rastreamento de bugs para ajudar nesse processo.
- **Métricas de código:**  Utilizar métricas para quantificar a qualidade do código. Isso inclui métricas de defeitos (bugs) e complexidade. Acompanhar o número de defeitos, sua gravidade e buscar reduzir a complexidade do código.

### Novidade para mim:

- Metricas de código
- Analisar Bugs

### O que já era conhecido por mim:

- Princípio dos 4 Olhos
- Integração Continua
- Convenções no Código
- Testes

### Comentário

O video e o [artigo em que o vídeo se baseia](https://betterprogramming.pub/things-that-you-can-do-to-improve-code-quality-c746c30e7521) destaca a importância de cuidar da qualidade do código para evitar problemas futuros e facilitar a manutenção do projeto. Ele enfatiza que a qualidade do código é responsabilidade de todos os membros da equipe, independentemente do papel que desempenhem. Algumas das práticas recomendadas incluem a revisão de código por pares, a integração contínua para obter feedback rápido, o uso de convenções de codificação para garantir consistência, a realização de testes abrangentes, a análise de bugs para aprendizado e a medição de métricas de qualidade. É ressaltado que o código de alta qualidade paga por si mesmo a longo prazo, promovendo a reutilização, reduzindo o tempo gasto na correção de bugs e facilitando a entrada de novos membros na equipe.
