Grupo: Jean Luca Lins, João Pedro Garcia M Costa, Matheus Lopes, Miguel Battendieri e Pedro Vendrametto.

Pesquisa Aprofundada

O Apache Kafka é um sistema de armazenamento de dados de forma distribuída otimizado para ingestão e processamento de dados de streaming que são atualizados em tempo real. Geralmente, tais dados são gerados por inúmeras fontes, que normalmente enviam tais registros de forma simultânea e contínua. Uma plataforma de transmissão precisa lidar com esse fluxo constante de dados e processá-los de forma sequencial e incremental, a fim de garantir que não haverá nenhuma confusão ou erro. Nesta área, sabemos o quão caros e danosos podem ser erros de operação, mesmo que eles durem poucos segundos.
O Kafka oferece a seus clientes três principais funções. Elas são:
- Publicar e assinar fluxos de registros.
- Armazenar fluxos de registros de forma eficaz na ordem em que tais registros foram armazenados. 
- Processar fluxos de registros em tempo real.
Sendo assim, o Kafka atua na combinação entre mensagens, armazenamento e processamento de dados, permitindo a construção de análises históricas e 100% atualizadas acerca do tema em que uma determinada base de dados aborda.
O Kafka combina dois modelos de mensagens para operar. Tais modelos são filas e publicação-assinatura. O enfileiramento permite que o processamento de dados seja distribuído de forma escalável e em várias instâncias do consumidor, enquanto a publicação-assinatura envia mensagens padronizadas para cada um dos clientes. 

Definição do cenário de IA

Cenário de Inteligência Artificial: Detecção de Fraudes em Tempo Real

O cenário de Inteligência Artificial escolhido é um Sistema de Detecção de Fraudes em Tempo Real aplicado a um e-commerce. Neste ambiente, a arquitetura orientada a eventos, gerenciada pelo Apache Kafka, é utilizada para conectar o "Sistema de Vendas" (Produtor) a um modelo de Machine Learning (Consumidor). Assim que um cliente finaliza uma compra, o sistema publica essa transação no tópico compras_site do Kafka. Imediatamente, um grupo de consumidores dedicado à IA (o Grupo IA_Antifraude) consome essa mensagem e avalia a probabilidade de a transação ser fraudulenta em questão de milissegundos, antes mesmo de o "Grupo Estoque" separar o produto ou o "Grupo E-mail" enviar o recibo de confirmação.

Tipos de Dados Transmitidos 

Neste ecossistema, a comunicação e o processamento dependem da transição rápida entre três formatos de dados principais:
- Mensagens em formato JSON (JavaScript Object Notation): A transação original gerada pelo site trafega pelo Kafka no formato JSON. Ela contém dados estruturados em texto, como: {"id_compra": 8492, "valor_total": 4500.00, "id_usuario": "A19", "ip_origem": "192.168.x.x", "horario": "2023-10-27T14:30:00"}.
- Tensores (Tensors): Ao chegar no microsserviço da IA, os dados do JSON são extraídos, normalizados e convertidos em tensores. Um tensor é uma estrutura matemática multidimensional (como uma matriz de números) que representa as características da compra de forma codificada.
- Fluxos de Texto/Eventos (Data Streams): Os dados não são enviados em lotes (arquivos fechados no fim do dia), mas sim como um fluxo contínuo e ininterrupto de eventos geridos pelo Kafka.
Justificativa e Relevância dos Dados para o Sistema de IA - A escolha e a transformação desses dados são estritamente alinhadas às necessidades técnicas de um sistema antifraude:
- JSON para Interoperabilidade: O JSON é extremamente leve e legível universalmente. Sua relevância está em permitir o desacoplamento perfeito no Kafka: o site que produz a venda (talvez feito em JavaScript/Node) envia um JSON, e a IA que consome (geralmente feita em Python) consegue lê-lo sem problemas de compatibilidade.
- Tensores para Processamento Neural: Modelos de Deep Learning ou árvores de decisão avançadas não "entendem" textos como um endereço IP ou um nome. A relevância do tensor está em transformar informações comportamentais em cálculos matemáticos puros, permitindo que as placas de vídeo (GPUs) ou processadores da IA calculem os padrões de anomalia (fraude) de forma vetorizada e ultrarrápida.
- Fluxo Contínuo (Streaming) para Baixa Latência: O envio de dados em fluxo via Kafka é a espinha dorsal do projeto. A natureza da detecção de fraudes exige que o dado seja consumido e processado no exato segundo em que a compra ocorre. Se utilizássemos planilhas estáticas ou processamento em lote, a fraude só seria descoberta horas depois, quando o produto já estivesse a caminho do fraudador.

Referências:	

https://aws.amazon.com/pt/what-is/apache-kafka/ 
https://kafka.apache.org/#:~:text=Apache%20Kafka%20is%20an%20open%2Dsource%20platform%20for,of%20data%2C%20hundreds%20of%20thousands%20of%20partitions 
https://www.ibm.com/br-pt/think/topics/apache-kafka 

