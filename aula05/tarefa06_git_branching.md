# Tarefa 006: Git Branching - 28/04/2023

1. Qual o nome do branch padrão do Git?
2. O que o comando `git branch nome` realiza?
3. Como criar um branch a partir de um commit específico?
4. Em um repositório, qual o efeito do comando `git checkout -b bugfix/234`?
5. Qual o comando para se alternar para um branch de nome **experimento2**?
6. Em um repositório com dois branches, **b1** e **b2**, onde b1 é o corrente, qual o efeito do comando `git branch`?
7. O que o comando `git checkout -b` nome faz?
8. Qual a função do comando `git branch -d teste`?
9. Durante o desenvolvimento de um software é comum, por exemplo, utilizar um novo recurso por meio de experimentação. Talvez uma nova tecnologia, uma nova biblioteca que pode ser útil ao que está em desenvolvimento, ou até mesmo uma nova versão de um produto já empregado. Para que o uso deste novo recurso não interfira com o que é considerado pronto, um branch pode ser criado para a experimentação. Código que for criado para a experimentação existirá apenas no branch criado. Se eventualmente o experimento demonstrar um resultado satisfatório, as alterações realizadas no branch poderão ser incorporadas no que é considerado pronto, ou seja, no branch principal (master). Esta última ação é conhecida por merge. Neste item, crie uma sequência de comandos que simula um caso simples de criação e uso seguido de merge empregando um branch para ilustrar uma experimentação conforme acima. A sequência deve incluir, obrigatoriamente: (a) criação de um ou mais branches; (b) chaveamento para pelo menos dois branches e (c) merge.

## Respostas

1. O nome do branch padrão do git é **main**, anteriorimente o nome padrão era **master**.
2. `git branch nome` cria uma nova branch (ramificação) no git com o nome especificado, a partir do commit atual.
3. `git branch <nome_da_branch> <hash_do_commit>` é o comando que cria uma branch a partir de um commit específico
4. `git checkout -b bugfix/234` cria uma nova branch chamada bugfix/234 e imediatamente muda o seu repositório Git para essa branch.
5. O comando para alternar para uma branch de nome experimento2 é `git checkout experimento2`
6. `git branch` lista todas as branches disponíveis no repositório local, logo ira listar as branches b1 (com asterisco, marcando a branch corrente) e b2.
7. `git checkout -b <nome>` é uma abreviação para a sequência de comandos `git branch <nome>` (que cria a nova branch) e `git checkout <nome>` (que muda para a nova branch).
8. `git branch -d teste` tem a função de deletar o branch local chamado "teste". Isso só é possível se não houver commits unmerged na branch
9. Sequencia de comandos:
   - `git branch nova_funcionalidade`
   - `git checkout nova_funcionalidade`
   - `git add nova_func.cpp`
   - `git commit -m "Adiciona nova_func.cpp"`
   - `git checkout master`
   - `git merge nova_funcionalidade`
