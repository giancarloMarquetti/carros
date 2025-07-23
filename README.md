# 🚗 Catálogo de Carros

Um sistema web robusto desenvolvido com Django, focado em **divulgar e gerenciar carros disponíveis para revenda ou em uma loja**. Este projeto foi construído com ênfase no backend, oferecendo uma solução completa para exibir seu inventário de veículos de forma eficiente e moderna.

---

## ✨ Funcionalidades Principais

* **Autenticação de Usuários:** Sistema completo de cadastro e login para gerenciamento de acesso.
* **CRUD de Veículos:** Funcionalidades de Criar, Ler, Atualizar e Deletar (CRUD) para gerenciar o catálogo de carros.
* **Gestão de Inventário com Signals:** Utiliza os `signals` do Django para gerenciar o inventário de carros de forma reativa, garantindo que as quantidades e status sejam atualizados automaticamente com base nas operações do sistema.
* **Listagem e Detalhes:** Exibição intuitiva dos carros em um catálogo com cards responsivos, incluindo fotos, marca, modelo, ano e valor, além de páginas de detalhes para cada veículo.
* **Sistema de Busca:** Ferramenta de pesquisa para encontrar carros específicos por diversas características.
* **Geração Automática de Bio com OpenAI:** Integração com a **API da OpenAI** para gerar descrições (bios) automáticas e criativas dos veículos, caso o usuário não forneça uma.
* **Design Responsivo:** Layout adaptável para proporcionar uma excelente experiência em desktops, tablets e smartphones.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:**
    * Python
    * Django
* **Frontend:**
    * HTML5
    * CSS3
    * JavaScript
* **Banco de Dados:**
    * PostgreSQL (em ambiente de produção)
    * SQLite (padrão do Django para desenvolvimento)
* **Outros:**
    * API OpenAI

---

## 🚀 Como Executar o Projeto Localmente

Siga estas instruções para configurar e rodar o projeto em sua máquina:

### Pré-requisitos

Certifique-se de ter o **Python** (preferencialmente 3.9+) e o **pip** (gerenciador de pacotes do Python) instalados em seu sistema.

```bash
### 1. Clonar o Repositório

git clone [https://github.com/giancarloMarquetti/catalogo-de-carros.git](https://github.com/giancarloMarquetti/catalogo-de-carros.git) # Ajuste o nome do repositório se for diferente
cd catalogo-de-carros # Navegue até a pasta raiz do projeto

### 2. Criar e Ativar o Ambiente Virtua

python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

### 3. Instalar as Dependências

pip install -r requirements.txt

### 4. Configurar Variáveis de Ambiente

Edite o arquivo carros/app/settings.py para definir a senha do seu banco de dados PostgreSQL. Para a API da OpenAI, edite o arquivo openai_api/client.py para inserir sua chave.

Banco de Dados (em carros/app/settings.py):
# Exemplo (ajuste conforme sua configuração real do PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'seu_banco_de_dados',
        'USER': 'seu_usuario',
        'PASSWORD': 'SEU_PASSWORD_AQUI', # <-- Defina sua senha aqui
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

API Key da OpenAI (em openai_api/client.py):
# Exemplo (ajuste conforme a estrutura do seu client.py)
api_key = "SUA_API_KEY_DA_OPENAI_AQUI" # <-- Insira sua chave aqui

### 5. Aplicar Migrações do Banco de Dados

python manage.py migrate

### 6. Criar um Superusuário (Opcional)

python manage.py createsuperuser

### 7. Iniciar o Servidor de Desenvolvimento

python manage.py runserver
```

## ☁️ Configuração para Implantação na AWS
Este projeto foi configurado com as melhores práticas para facilitar a implantação em serviços da Amazon Web Services (AWS). Embora os detalhes específicos de deploy (como Dockerfiles, arquivos de configuração para Elastic Beanstalk, ECS, etc.) possam variar e não estejam incluídos neste README, a estrutura do projeto e o uso de PostgreSQL como banco de dados (comumente utilizado com AWS RDS) são compatíveis com ambientes de nuvem.

Pontos importantes para deploy na AWS:

Variáveis de Ambiente: Utilize variáveis de ambiente para gerenciar configurações sensíveis (chaves de API, credenciais de banco de dados) na AWS, em vez de hardcodar no código.

Static Files (S3): Recomenda-se configurar o Django para servir arquivos estáticos (CSS, JS, imagens) através do Amazon S3 para alta performance e escalabilidade.

Banco de Dados (RDS): O PostgreSQL é um excelente candidato para ser hospedado no Amazon RDS, um serviço de banco de dados gerenciado.

Serviço de Aplicação: Considere usar serviços como AWS Elastic Beanstalk (para deploy rápido e gerenciado), Amazon ECS (para contêineres Docker) ou EC2 (para maior controle sobre a infraestrutura).

## 📄 Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

## 👤 Autor
Giancarlo Marquetti
GitHub: https://github.com/giancarloMarquetti
LinkedIn: https://www.linkedin.com/in/giancarlo-marquetti-2b3263344/
