import json
import numpy as np
from kafka import KafkaConsumer

# Configura o consumidor para ler o tópico "compras_site" e participar do grupo "IA_Antifraude"
consumidor = KafkaConsumer(
    'compras_site',
    bootstrap_servers=['192.168.183.180:9092'],
    group_id='Grupo_IA_Antifraude',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("🧠 Sistema IA Antifraude Iniciado. Aguardando eventos no Kafka...")

for mensagem in consumidor:
    dados_json = mensagem.value

    # 1. Extração de Features (Características)
    valor = dados_json['valor_total']
    score = dados_json['score_usuario']

    # 2. Transformação em Tensor (Vetor matemático de 1 dimensão usando numpy)
    # Modelos de IA não leem "id_usuario", leem números brutos normalizados.
    tensor_ia = np.array([valor / 5000.0, score]) # Normalizando o valor para ficar entre 0 e 1

    # 3. Avaliação Simples (Simulando uma rede neural)
    # Se o tensor representar um valor alto (próximo a 1) e um score baixo, é fraude!
    probabilidade_fraude = (tensor_ia[0] * 0.7) + ((1 - tensor_ia[1]) * 0.3)

    print("-" * 50)
    print(f"📥 Recebido JSON: {dados_json}")
    print(f"⚙️  Convertido para Tensor: {tensor_ia}")

    if probabilidade_fraude > 0.6:
        print(f"🚨 ALERTA DE FRAUDE! Probabilidade: {probabilidade_fraude:.2f}")
    else:
        print(f"🟢 Transação Aprovada. Probabilidade: {probabilidade_fraude:.2f}")
