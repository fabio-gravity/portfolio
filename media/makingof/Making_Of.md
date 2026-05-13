# Diário de Bordo: Processo de Modelação do Portfólio

Este documento regista a evolução, as decisões e os erros corrigidos durante 
a fase de modelação da base de dados do projeto de Portfólio em Django.

## 1. Fotografias do DER e Apontamentos

O planeamento foi feito à mão em papel antes de passar para código. 
As fotografias seguintes documentam esse processo:

### Modelos e Atributos
![Modelos Tecnologia, TFC, Competências e Formação](media/makingof/6_1.jpeg)

![Modelo Making Of](media/makingof/6_2.jpeg)

### Diagrama Entidade-Relação
![DER desenhado à mão](media/makingof/6_3.jpeg)

### Modelos Complementares
![Modelos Licenciatura, Unidade Curricular, Docente e Projetos](media/makingof/6_4.jpeg)

## 2. Evolução do Modelo e Correção de Erros

### Versão 1 (Rascunho Inicial)
* **Erro Identificado:** O primeiro rascunho tinha entidades isoladas. 
  As `Formações` e as `Competências` não estavam ligadas ao resto do modelo, 
  tornando impossível cruzar informação entre o percurso académico e os projetos.
* **Correção:** Redesenhei o DER para criar uma rede coerente. 
  A `Licenciatura` passou a ser o ponto central do percurso académico, 
  agregando as `Unidades Curriculares`. As `Competências` passaram a ligar-se 
  tanto aos `Projetos` como às `Formações` através de relações N:M.

### Versão 2 (Ajuste de Relações)
* **Erro Identificado 1:** A relação entre `Licenciatura` e `TFC` estava 
  definida como 1:N. No entanto, no contexto do meu portfólio pessoal, 
  cada licenciatura culmina num único TFC.
* **Correção 1:** Alterei para `OneToOneField`, garantindo que cada 
  licenciatura tem no máximo um Trabalho Final de Curso.
* **Erro Identificado 2:** Faltavam atributos importantes previstos nos 
  apontamentos: imagens para as tecnologias, links de repositório nos 
  projetos, e datas nas formações.
* **Correção 2:** Adicionei `ImageField` para logos e imagens, `URLField` 
  para links GitHub e páginas de docentes, e `DateField` para ordenação 
  cronológica.

### Versão 3 (Implementação e Erros de Sintaxe)
* **Erro Identificado 3:** `IndentationError` ao tentar correr as migrações. 
  O `models.py` tinha espaços desalinhados que bloqueavam o Python.
* **Correção 3:** Realinhamento completo do código com indentação 
  consistente de 4 espaços por nível.
* **Erro Identificado 4:** O Django gerava plurais incorretos no painel 
  admin, como "Unidade curriculars" e "Tfcs".
* **Correção 4:** Adição de `class Meta` com `verbose_name` e 
  `verbose_name_plural` em português em cada modelo.

### Versão 4 (Ajustes após análise do JSON dos TFCs)
* **Erro Identificado 5:** O modelo `TFC` original tinha um 
  `OneToOneField` para `Licenciatura` e campos simples (`nome`, 
  `descricao`, `classificacao`). No entanto, o ficheiro JSON dos TFCs 
  continha campos adicionais não previstos: `autores`, `orientadores`, 
  `licenciaturas` (como texto), `sumario`, `link_pdf`, `imagem`, 
  `palavras_chave`, `areas`, `tecnologias_usadas` e `rating`.
* **Correção 5:** Reestruturei o modelo `TFC` para incluir todos os 
  campos do JSON. Removi o `OneToOneField` para `Licenciatura` e 
  substituí por um campo `CharField` para `licenciaturas`, uma vez que 
  os dados do JSON contêm nomes de cursos como texto livre.

### Versão 5 (Enriquecimento dos modelos após carregamento de dados)
* **Erro Identificado 6:** Ao inserir dados reais no Admin, percebi 
  que faltavam atributos úteis em vários modelos:
  - `Docente`: faltava `imagem` para mostrar foto do professor
  - `Formacao`: faltava `descricao` e `certificado_url`
  - `Competencia`: faltava `tipo` para separar Hard Skills de Soft Skills
  - `Projeto`: faltava ligação à `UnidadeCurricular`
  - `Licenciatura`: faltava `sigla`, `descricao` e `ects_total`
  - `UnidadeCurricular`: faltavam campos detalhados da API 
    (`ano_curricular`, `semestre`, `ects`, `objetivos`, `metodologia`, 
    `programa`, `bibliografia`, `avaliacao`)
  - `MakingOf`: faltava campo `uso_ia` para documentar uso de IA
* **Correção 6:** Adicionei todos os atributos em falta aos modelos 
  correspondentes, fiz as migrações e atualizei o admin.

## 3. Carregamento de Dados via JSON

### TFCs
O ficheiro `tfcs_2025_.json` foi analisado e verificou-se que continha 
campos adicionais não previstos no modelo inicial. O modelo `TFC` foi 
atualizado para incluir estes campos e foi criado o script 
`data/carrega_tfcs.py` para automatizar o carregamento via ORM Django.

O script utiliza `get_or_create` para evitar duplicação de dados caso 
seja executado múltiplas vezes, verificando pelo campo `titulo`.

## 4. Carregamento de Dados via API (Curso e Unidades Curriculares)

Utilizei a API pública da Lusófona para descarregar os dados do curso 
LEI (código 260) e de cada Unidade Curricular. O script 
`data/download_curso.py` faz o download dos JSONs para a pasta 
`data/files/`. O script `data/carrega_curso.py` lê esses JSONs e 
carrega os dados na base de dados usando o ORM Django.

Os dados carregados incluem: nome, código, ano curricular, ECTS, 
natureza, objetivos, apresentação, metodologia, programa, bibliografia 
e avaliação.

## 5. Justificação das Decisões de Modelação

**1. Licenciatura** — Entidade central do percurso académico. `CASCADE` 
nas Unidades Curriculares garante que não ficam dados órfãos. 
`PositiveIntegerField` para ECTS e duração bloqueia valores negativos. 
Adição de `sigla` e `ects_total` permite apresentar informação 
resumida do curso.

**2. Docente** — Entidade separada em vez de simples campo de texto, 
para resolver a relação N:M (um professor dá várias UCs, uma UC pode 
ter vários professores). `URLField` para ligar à página oficial. 
`ImageField` para mostrar foto do professor no frontend.

**3. Unidade Curricular** — `ForeignKey` para Licenciatura (1:N). 
`ImageField` para cartões visuais. Campos detalhados da API (objetivos, 
metodologia, programa, bibliografia, avaliação) enriquecem o portfólio 
e permitem consultar informação completa de cada disciplina.

**4. Projeto** — Tabela central que cruza várias entidades: liga-se 
a Tecnologias (N:M), Competências (N:M) e à UC de origem (FK). 
`URLField` para o link GitHub é essencial num portfólio de desenvolvedor.

**5. Tecnologia** — Entidade separada ligada por N:M aos Projetos. 
Evita repetição: "Python" é escrito uma vez e ligado a vários projetos. 
`interesse` (1-5) permite ordenar a stack favorita no topo.

**6. TFC** — Modelo reestruturado para refletir os dados do JSON. 
Campos `palavras_chave`, `areas` e `tecnologias_usadas` permitem 
filtragem e pesquisa. `rating` permite ordenar por relevância.

**7. Competência** — Liga N:M a Projetos. `tipo` permite separar 
Hard Skills de Soft Skills no currículo digital. `nivel` quantifica 
a proficiência.

**8. Formação** — `DateField` com `ordering = ['-data_inicio']` ordena 
automaticamente do mais recente para o mais antigo. `certificado_url` 
permite ligar a certificados online.

**9. Making Of** — Auto-documentação do processo. Campos `decisoes_tomadas`, 
`erros_correcoes` e `uso_ia` garantem transparência técnica e cumprem 
os critérios de avaliação.

## 6. Uso de Inteligência Artificial

Durante este processo utilizei IA (Claude da Anthropic) como 
peer-programmer e tutor. A IA foi utilizada para:
* Debug de erros de configuração e sintaxe
* Atualização dos ficheiros `settings.py` e `urls.py`
* Estruturação dos modelos Django a partir dos apontamentos em papel
* Criação dos scripts de carregamento de dados JSON e API
* Criação do Making Of em Markdown
* Todas as decisões finais de modelação foram tomadas por mim, 
  com a IA a servir de suporte técnico