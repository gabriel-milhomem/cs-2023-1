# Tarefa Grupo 005: Git Exercícios - 28/04/2023

Responda as questões abaixo (exercite os comandos do git correspondentes). Lembre-se de que o “interessante” não é exatamente o conjunto de respostas, mas o processo de obtê-las e a experiência obtida com a execução dos comandos.

## Perguntas

1. Qual o comando para obter a versão instalada do Git?
2. Qual o efeito da execução de cada um dos comandos abaixo?
  a. git help
  b. git help checkout
  c. git help merge
  d. git init
  e. git add --all
  f. git add -u
  g. git config -l
  h. git mv a.txt b.txt
  i. git reset --hard
  j. git log -27
3. O fluxo “clássico” de interação com o Git é algo como “alterar um ou mais arquivos”, “acrescentar essas mudanças para serem contemplados no próximo commit” e, finalmente, executar um “commit”. Quais os comandos necessários para realizar os dois últimos “passos” desse fluxo?
4. Qual o comando deve ser executado para identificar o que foi alterado desde o último “commit”?
5. Em um dado repositório, arquivos simplesmente copiados para lá, ou seja, _untracked_, podem ser exibidos/identificados com que comando?
6. Qual o comando para efetuar um _commit_?
7. Qual o comando que devemos empregar para descartar mudanças ocorridas no arquivo teste.txt, por exemplo?
8. O que deve ser feito para que um determinado diretório do seu repositório seja ignorado pelo Git? Faça uma busca por **.gitignore**.
9. O que acontece se o seu repositório local for acidentalmente removido?
10. Como clonar um repositório remoto?
11. Em alguns cenários **git log** pode produzir extensos resultados. Se houver interesse em visualizar o histórico de um repositório, onde cada mudança é fornecida exatamente em uma única linha, qual o comando que deve ser empregado?
12. Em qual arquivo o Git armazena informações de configuração empregadas por usuário?
13. Qual o comando para criar um repositório local?
14. Qual o nome do diretório criado pelo Git quando se executa o comando **git init**?
15. Qual o comando para adicionar todos os arquivos modificados? (Aqueles para os quais **git status** identificam como **modified**?)
16. O Git faz uso do valor de hash conhecido por SHA1. O que isto significa? Qual o propósito? O que é SHA1?
17. Qual a palavra para indicar o último _commit_ em vez do valor de hash SHA1 correspondente?
18. Quando se cria dois arquivos usando um editor de texto qualquer e, na sequência, executamos o comando **git add -u**, os dois arquivos criados passam de _untracked_ para _new file_?
19. Qual o efeito da execução dos dois comandos abaixo, nesta ordem, em um dado repositório?
**git reset --soft HEAD~1**
**git reset --hard**
20. Após o emprego de um ambiente integrado de desenvolvimento (IDE), é comum a criação de arquivos e diretórios. Qual o comando que podemos empregar para remover arquivos e diretórios _untracked_?
21. Qual o nome do arquivo no qual podemos inserir a indicação para o Git de arquivos e diretórios a serem ignorados?
22. Quando se cria o arquivo _MinhaClasse.class_ em um dado diretório e desejamos que arquivos com a extensão .class, como neste caso, sejam ignorados por todos os membros de uma equipe que estão contribuindo com um dado projeto, como devemos proceder?
23. jQuery é uma famosa biblioteca em JavaScript. Consulte detalhes em [jQuery](http://jquery.com). O repositório correspondente encontra-se em [gitRep](https://github.com/jquery/jquery.git). Faça o clone deste repositório.
24. No repositório **jqueryrepo**, criado no passo anterior, qual o efeito do comando
**git shortlog -sne**?
25. No repositório **jqueryrepo**, qual o efeito de **git remote -v**?
26. Um repositório Git pode ser etiquetado ao longo do tempo. Ou seja, _commits_ específicos podem ser “marcados” ou “etiquetados” para facilitar referências posteriores. Para listar todas as “etiquetas” (_tags_) estabelecidas para um dado repositório, qual comando deve ser executado?
27. Caso um dado repositório retorne muitas “marcas” ou “etiquetas” para o comando **git tag**, como retornar apenas aquelas que atendem a determinado padrão, por exemplo, iniciadas por 2.0?
28. Qual o efeito do comando **git tag -a 3.4-gold -m “minha versão ouro”**?
29. Após executado o comando acima, qual o efeito de **git show 3.4-gold**?
30. O que o comando **git push origin 3.4-gold** teria como efeito?
31. Após executar um commit, qual o efeito de **git commit --amend**?
32. Após executar **git add x.txt**, qual o efeito de **git reset HEAD x.txt**?
33. Após alterar o conteúdo de um arquivo committed em passo anterior, qual o efeito do comando **git checkout -- a.txt**?
34. Qual a diferença entre os comandos **git reset HEAD a.txt** e **git checkout -- a.txt**?
35. Veja como interpretar o resultado de git diff [aqui](https://medium.com/therobinkim/how-to-read-a-git-diff-6c87a9dc47c5). Execute, em um dos seus projetos, o comando **git diff HEAD~1 HEAD** e certifique-se de que entende o resultado apresentado.

### Respostas

1. `git --version` mostra a versão do git instalada
- 2a `git help` mostra o manual do git e os comandos disponíveis para uso
- 2b `git help checkout` abre a documentação do git pela web sobre o comando o checkout, para consulta
- 2c `git help merge` abre a documentação do git pela web sobre o comando merge, para consulta
- 2d `git init` inicializa um repositório git
- 2e `git add --all` adiciona todas as modificaçoões, incluindo novos arquivos, em staged para ser commitado no futuro
- 2f `git add -u` é mais seletivo, pois adiciona as mudanças feitas em arquivos jã existentes no staging area
- 2g `git config -l` é usado para listar as configurações do Git em um determinado diretório
- 2h `git mv a.txt b.txt` renomeia o arquivo "a.txt" para "b.txt" no repositório Git
- 2i `git reset --hard` é usado para desfazer todas as mudanças locais e restaurar o diretório de trabalho para o último commit.
- 2j `git log -27` mostra os ultimos 27 commits no histórico do git
3. `git add .` para adicionar todas as alterações realizadas e `git commit -m "mensagem"` para realizar o commit
4. `git diff` é o comando que identifica o que foi alterado desde o último commit
5. `git status` exibe os arquivos que não estão sendo rastreados pelo Git na seção "untracked files"
6. `git commit -m "mensagem"` é o comando para efetuar um commit
7. `git checkout -- nome_do_arquivo` descarta as mudanças em um arquivo para o estado em que estava no último commit
8. Deve se criar um arquivo chamado `.gitignore` na raiz do repositório e adicionar o nome do diretório que deseja que o Git ignore
9. É possível recuperá-lo por meio do `git clone`. Isso ira baixar uma cópia do repositório remoto para o diretório local
10. `git clone <url_repositorio>` é o comando para clonar um repositório remoto
11. `git log --oneline` visualiza o histórico com uma linha por mudança
12. `.gitconfig` é o arquivo que contem as configs do usuário
13. `git init` cria um repositório local
14. é chamado de diretório raiz do repositório
15. `git add -u` é o comando para adicionar todos os arquivos modificados
16. `SHA1` é um algoritmo de hash criptográfico, tem o propósito de produzir uma assinatura digital única para um arquivo que pode ser verificado
17. `HEAD` é a palavra que indica último commit
18. Não, `git add -u` adiciona apenas os arquivos que foram modificados ou excluídos, não os novos.
19. `git reset --soft HEAD~1` desfaz o último commit e mantém as alterações no estado "staged". `git reset --hard` descarta as alterações e retorna o repositório para o último commit
20. `git clena -f -d` remove arquivos e diretórios untracked
21. `.gitignore` é o arquivo que podemos inserir para indicar ao Git quais arquivos e diretórios serão ignorados
22. Pode-se adicionar a linha `*.class` no arquivo `.gitignore` para ignorar todos os arquivos com extensão .class
23. `git clone https://github.com/jquery/jquery.git` clona o repositório do jQuery
24. `git shortlog -sne` exibe um resumo de commits do repositório. Mostra o número de commits feitos por cada autor, em ordem decrescente.
25. `git remote -v` exibe os repositórios remotos vinculados ao repositório local, incluindo seus nomes e URLs.
26. `git tag` exibe uma lista de todas as tags existentes
