# Tarefa 002 - 17/04/2022 - Pesquisa Rest API

1. Elaborar uma pesquisa sobre o tema "_Rest API_".
2. Elaborar um texto **no formato markdown** de pelo menos uma página, descrito com suas próprias palavras, destacando:

- As definições dos conceitos envolvidos;
- As principais características deste conceito (pelo menos umas cinco).

## O que é API REST ?

É um conjunto de rotinas, padrões de programação e protocolos que permite a comunicação entre diferentes softwares.

Uma API (Interface de Programação de Aplicações em ingles), é um conjunto de rotinas, padrões de programação e protocolos que integram um usuário a uma aplicação, permitindo que ele acesse e faça uso das funcionalidades do software em questão. Uma API funciona como um mediador, ou comunicador, entre o usuário e o sistema ou entre diferentes softwares. Deste modo, ela facilita o acesso e o desenvolvimento de software para a internet

Uma Rest API é uma API que segue o modelo arquitetural Rest (Representational State Transfer), que é um conjunto de princípios para o desenvolvimento de serviços Web. O Rest é baseado no protocolo HTTP e utiliza as operações GET, POST, PUT e DELETE para manipular recursos identificados por URLs.

### Principais Características de uma REST API ?

- **Cliente-Servidor**: Trata a respeito da separação de responsabilidades, ou seja, separar as preocupações de interface do usuário (User Interface) do banco de dados, abstraindo a dependência entre os lados clientes/servidor e permitindo a evolução desses componentes sem impacto e quebra de contrato.

- **Estado das requisições**: As requisições para uma Rest API devem ser autocontidas, ou seja, todas as informações necessárias para executar a requisição devem estar presentes nela mesma, não dependendo de um estado de sessão previamente armazenado no servidor.

- **Armazenável em cache**:
Como uma API sem estado pode aumentar sobrecarga de solicitação gerenciando grandes cargas de chamadas de entrada e saída, um design de API REST deve armazenar dados em cache.
Se uma resposta puder ser armazenada em cache, o cache do cliente terá o direito de reciclar os dados de resposta para solicitações semelhantes no futuro.

- **Operações HTTP**
As operações HTTP são padronizadas e definidas pelo protocolo HTTP. As quatro operações principais são:
  - GET: solicita a representação de um recurso específico.
  - POST: cria um novo recurso.
  - PUT: atualiza um recurso existente.
  - PATCH: atualiza parcialmente um recurso existente.
  - DELETE: remove um recurso existente.
  - HEAD: retorna os cabeçalhos HTTP sem o corpo da resposta.

- **Recursos identificados por URI**
Os recursos da API são identificados por URLs únicas (URIs). Cada recurso deve ter sua própria URI. Os recursos podem ser qualquer coisa, como um usuário em um sistema, um produto em um catálogo online ou uma transação financeira. Exemplo: a URL http://api.minhaempresa.com.br/usuarios/123 representa um usuário específico com ID 123. Dessa forma, ao acessar essa URI, a API retornaria as informações do usuário com o ID 123 em um formato bem definido, como JSON ou XML.

- **Representação dos recursos**
Cada recurso deve ser representado em um formato bem definido, geralmente JSON (JavaScript Object Notation) ou XML (Extensible Markup Language). Essa representação é chamada de payload ou corpo da mensagem.

- **Autenticação e autorização**
As Rest APIs geralmente requerem autenticação e autorização para garantir a segurança dos dados. A autenticação é o processo de identificação do usuário, enquanto a autorização é o processo de verificar se o usuário tem permissão para acessar determinado recurso.