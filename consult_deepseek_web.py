import os
import json
import urllib.request

api_key = 'v1.CmQKHHN0YXRpY2tleS1lMDB4ZTQxaG50amRrNXg5dGcSIXNlcnZpY2VhY2NvdW50LWUwMHBhOXhwcHhzNHYyY2ZqMDIMCK3v7tYGEJu5--sBOgwItvKGogcQwM-XqwFAAloDZTAw.AAAAAAAAAAGk3wOYsUIHmuowESG-zw-rzpO-wlih0bEptEi0nq20gxkEnlXrAmrofg-lQl5syJNkF8W4cYLOYo1JIIwzceYG'
url = 'https://api.tokenfactory.nebius.com/v1/chat/completions'
model = 'deepseek-ai/DeepSeek-V4.1-Flash'

prompt = """Actúa como Lead Frontend & Systems Architect para nuestra Startup: "SaaS B2B de Transparencia Radical y Gobernanza por IA".
El usuario fundador quiere:
1. "Dame ya la primera página web y empecemos a desarrollar la estructura".

Esta primera página web NO es una landing decorativa típica con marketing vacío. Es la INTERFAZ PÚBLICA DE TRANSPARENCIA RADICAL Y GOBERNANZA EN VIVO (Live Governance Ledger & Client Democracy Console).
Debe mostrar con sobriedad y contundencia técnica (estética Linear, Bloomberg, Stripe, Datadog):
1. **Header Institucional:** Estado del sistema y la declaración del modelo (SaaS B2B Auditado por IA).
2. **Ledger Financiero en Tiempo Real (CFO Agent Feed):**
   - MRR en vivo.
   - Coste de servidores/GPUs en tiempo real.
   - Fondo de Reserva (Runway en meses: ej. 14.2 meses > umbral de 12m).
   - Excedente acumulado del mes elegible para rebaja de cuotas.
3. **El Consejo Ejecutivo de IA (Separación de Poderes en vivo):**
   - Agente CEO: Estado de arbitraje y propuestas del mes.
   - Agente CPO: Solicitudes de clientes agrupadas y demanda latente.
   - Agente CFO: Auditoría de nóminas y costes marginales.
   - Agente CTO: Uptime (99.98%), latencia (41ms), Veto Status: INACTIVO (Sistema Verde).
4. **Monitor de la Constitución (Hard Constraints):**
   - Invariante 1 (Salud 99.9%): OK.
   - Invariante 2 (Runway > 9m): OK (14.2m).
   - Invariante 3 (Carga humana <= 80%): OK (72%).
   - Invariante 4 (Fórmula Salarial pública): OK.
5. **Balota de Votación Mensual de Clientes (Democracia Activa):**
   - Propuesta 1: Nueva integración de nómina/ERP.
   - Propuesta 2: Módulo de analítica predictiva.
   - Propuesta 3: **Rebaja directa del 6.5% en la factura del próximo mes a todos los clientes** financiada con el superávit del CFO.
   - Interacción funcional para que el usuario pueda simular su voto con créditos ponderados.

Entrega:
1. La arquitectura técnica de carpetas para el frontend (`02_ENGINEERING/frontend`).
2. El código completo, autónomo, interactivo y estéticamente superior de esta primera página web (`index.html` con Tailwind CSS vía CDN, tipografía moderna monoespaciada/sans, gráficos limpios SVG/Canvas, y JavaScript interactivo de votación y telemetría en tiempo real) para que el fundador pueda abrirla y verla inmediatamente en su navegador.
"""

req = urllib.request.Request(
    url,
    headers={'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'},
    data=json.dumps({
        'model': model,
        'messages': [{'role': 'user', 'content': prompt}],
        'temperature': 0.2,
        'max_tokens': 4000
    }).encode('utf-8')
)

try:
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        content = data['choices'][0]['message']['content']
        with open(r"C:\Users\jordi\.gemini\antigravity\scratch\00_STARTUP_SAAS\00_CONTEXT\DECISIONS\deepseek_web_architecture.md", "w", encoding="utf-8") as f:
            f.write(content)
        print("SUCCESS: DeepSeek response saved.")
except Exception as e:
    print(f"ERROR: {e}")
