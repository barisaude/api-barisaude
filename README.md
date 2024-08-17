# Projeto de API REST para os aplicativos Barisaúde
<p>
  API com objetivo de gerenciar os dados manipulados pelos aplicativos Barisaúde,
  integrando um aplicativo Web, servindo de interface para médicos,
  e um aplicativo Mobile nativo, servindo de interface para os pacientes,
  com um banco de dados PostgreSQL.
</p>

---

#### Índice
<span style="white-space: nowrap;">
  <a href="#setup">Iniciando o projeto</a>
  &nbsp;&bull;&nbsp;
  <a href="#boa-conduta">Boa conduta</a>
  &nbsp;&bull;&nbsp;
  <a href="#arquitetura">Arquitetura</a>
  &nbsp;&bull;&nbsp;
  <a href="#testes">Testes</a>
</span>

---

<h3 id="setup">Iniciando o projeto</h3>

Para iniciar a desenvolver no projeto,
você precisará de [Python](https://python.org) na sua máquina.

Garanta que tenha o Python instalado e crie um ambiente virtual
para trabalhar com as dependencias do projeto

Para Linux:
```bash
  # Criar o ambiente virtual (uma pasta venv)
  python -m venv venv

  # Ative o ambiente
  source venv/bin/activate

  # Instalar as dependencias do projeto
  pip install -r requirements.txt
```

Para Windows:
```cmd
  <!-- Criar ambiente -->
  python -m venv venv

  <!-- Ativar ambiente no CMD -->
  .\venv\Scripts\activate.bat
  <!-- Ou no Powershell -->
  .\venv\Scripts\Activate.ps1

  pip install -r requirements.txt
```

Você pode iniciar o servidor localmente com o comando:
```bash
  python manage.py runserver
```

---

<h3 id="boa-conduta">Instruções de boa conduta</h3>

<span style="white-space: nowrap;">
  <a href="#style-guide">Style guide</a>
  &nbsp;&bull;&nbsp;
  <a href="#deps">Dependências do projeto</a>
</span>

<h4 id="style-guide">Mantendo o padrão de código</h4>

É importante que o código seja mantido em um padrão para que facilitar o desenvolvimento em conjunto.
Este é um lembrete para desenvolver este comportamento nos desenvolvedores deste projeto.

Além disso, o projeto foi configurado com um guia básico de estilização de código usando [EditorConfig](https://editorconfig.org/).
Alguns editores de código vem configurados para utilizar desta tecnologia, outros podem precisar da instalação de extensões.

Você pode verificar se seu editor preferido tem suporte para EditorConfig
na lista de editores [com suporte nativo](https://editorconfig.org/#pre-installed) ou [com extensões disponíveis](https://editorconfig.org/#download).

Para usuários do VS Code, o projeto já tem um arquivo de recomendações com a extensão do EditorConfig inclusa.

<h4 id="deps">Atualizando as dependências do projeto</h4>

Caso o desenvolvimento necessite a instalação de novas dependências,
lembre-se de atualizar o arquivo `requirements.txt`.

É recomendado usar a biblioteca [`pipreqs`](https://github.com/bndr/pipreqs) para recriar o arquivo:
```bash
  # Instale a biblioteca globalmente
  # deactivate (desligue o ambiente virtual)
  pip install pipreqs

  # Estando na raiz do projeto, exclua o arquivo `requirements.txt` e execute
  python -m pipreqs.pipreqs
  # Ou, force a sobreescrever o arquivo
  python -m pipreqs.pipreqs --force
```

---

<h3 id="arquitetura">Arquitetura</h3>

O projeto é construído usando Django REST Framework,
servindo como uma API REST baseado em JSON.

---

<h3 id="testes">Testes</h3>

<h4>Em construção... eu espero...</h4>
