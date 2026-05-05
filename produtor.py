import json
import time
import random
from kafka import KafkaProducer

# Configura o produtor para conectar ao Kafka local e enviar dados em JSON
produtor = KafkaProducer(
    bootstrap_servers=['192:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("🛍️  Sistema de Vendas (Produtor) Iniciado. Gerando vendas...")

try:
    while True:
        # Gera dados fictícios da compra
        compra = {
            "id_compra": random.randint(1000, 9999),
            "valor_total": round(random.uniform(50.0, 5000.0), 2),
            "id_usuario": f"U{random.randint(1, 100)}",
            "score_usuario": random.uniform(0.1, 1.0) # Simula um histórico do usuário
        }

        # Envia o JSON para o tópico
        produtor.send('compras_site', value=compra)
        print(f"✅ Venda publicada no Kafka: {compra}")

        time.sleep(3) # Espera 3 segundos até a próxima venda
except KeyboardInterrupt:
    print("\nEncerrando produtor.")
