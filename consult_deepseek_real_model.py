import urllib.request
import json

api_key = 'v1.CmQKHHN0YXRpY2tleS1lMDB4ZTQxaG50amRrNXg5dGcSIXNlcnZpY2VhY2NvdW50LWUwMHBhOXhwcHhzNHYyY2ZqMDIMCK3v7tYGEJu5--sBOgwItvKGogcQwM-XqwFAAloDZTAw.AAAAAAAAAAGk3wOYsUIHmuowESG-zw-rzpO-wlih0bEptEi0nq20gxkEnlXrAmrofg-lQl5syJNkF8W4cYLOYo1JIIwzceYG'
url = 'https://api.tokenfactory.nebius.com/v1/chat/completions'
model = 'deepseek-ai/DeepSeek-V4.1-Flash'

prompt = """Actúa como el más brillante Co-Founder y Chief Enterprise Architect.
El usuario fundador nos ha dado la directriz EXACTA y REAL de su startup:

"Quiero un CEO con un comité de dirección de IA que maneje una empresa donde ÚNICAMENTE alojen los mejores SaaS para empresa Open Source. El objetivo principal es dar lo mejor al menor precio del mercado esa es la idea. Es una startup desde cero. Nada de datos ficticios inventados ni números irreales: se necesita estructura real, modelo claro, arquitectura de catálogo de SaaS Open Source empresariales, cómo la IA gestiona los despliegues/operación al coste más bajo del mercado, y la interfaz real para que un cliente pueda entrar y usarla."

Desarrolla en profundidad:
1. TESIS Y MODELO DE NEGOCIO REAL:
   - Cómo sustituimos a los gigantes caros (Salesforce, Factorial, Zendesk, Slack, DocuSign, Jira) alojando las alternativas Open Source líderes mundiales (Twenty CRM, Odoo/ERPNext, Chatwoot, Mattermost, Documenso, Plane).
   - El modelo de precio: Coste de servidor/recursos + margen transparente mínimo de gestión. Por qué nadie puede competir en precio (sin burocracia humana).
2. EL ROL EXACTO DEL CEO Y COMITÉ DE DIRECCIÓN (IA):
   - CEO IA: Estrategia, acuerdos de infraestructura, relación y gobernanza.
   - CTO IA: Automatización de despliegues (Docker/K8s/Hetzner/OVH), mantenimiento, parches y backups sin coste laboral.
   - CFO IA: Facturación transparente por recursos reales al céntimo, optimización continua de costes.
   - CPO IA: Curaduría y benchmarking continuo de los mejores proyectos Open Source.
3. ESTRUCTURA REAL DEL PRODUCTO Y DE LA WEB DESDE CERO:
   - Catálogo de SaaS Open Source clasificado por departamento empresarial.
   - Comparador real de ahorro (€/mes por empleado vs software propietario cerrado).
   - Consola de despliegue de instancias para el cliente.
   - Panel del Comité Ejecutivo IA visible y transparente.
4. ESTRUCTURA DE CÓDIGO DEL PROYECTO (backend, frontend, agentes).

Sé quirúrgico, realista, profesional y enfocado en construir un negocio que funcione desde el día uno.
"""

req = urllib.request.Request(
    url,
    headers={'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'},
    data=json.dumps({
        'model': model,
        'messages': [{'role': 'user', 'content': prompt}],
        'temperature': 0.2,
        'max_tokens': 3500
    }).encode('utf-8')
)

try:
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        msg = data['choices'][0]['message']
        content = msg.get('content') or msg.get('reasoning_content') or ''
        with open(r"C:\Users\jordi\.gemini\antigravity\scratch\00_STARTUP_SAAS\00_CONTEXT\DECISIONS\deepseek_real_model.md", "w", encoding="utf-8") as f:
            f.write(content)
        print("SUCCESS: Real model blueprint saved.")
except Exception as e:
    print(f"ERROR: {e}")
