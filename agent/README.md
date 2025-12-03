# Agente de WhatsApp con LangChain

Este módulo implementa un agente inteligente de WhatsApp usando LangChain que se activa automáticamente cuando llegan mensajes.

## Estructura

-   **`tools.py`**: Define la herramienta `send_whatsapp_message` para enviar mensajes de WhatsApp
-   **`whatsapp_agent.py`**: Configura el agente de LangChain con GPT-4o-mini y las herramientas disponibles

## Características

✅ **Agente inteligente**: Usa GPT-4o-mini para procesar mensajes de forma conversacional
✅ **Herramienta de envío**: Puede iniciar conversaciones enviando mensajes a números de WhatsApp
✅ **Integración flexible**: Puede integrarse con cualquier sistema de mensajería
✅ **Manejo de errores**: Gestión robusta de excepciones

## Uso

### Desde el módulo whatsapp

```python
from agent.whatsapp_agent import process_whatsapp_message

# Procesar un mensaje entrante
response = process_whatsapp_message(
    sender_number="+5491112345678",
    message_text="Hola, ¿cómo estás?"
)
print(response)
```

### Ejemplo de uso de la herramienta

Si un usuario pregunta: "Envía un mensaje a +5491112345678 diciendo hola"

El agente automáticamente:

1. Detecta la intención de enviar un mensaje
2. Usa la herramienta `send_whatsapp_message`
3. Envía el mensaje al número especificado
4. Confirma al usuario que el mensaje fue enviado

## Variables de entorno requeridas

```env
OPENAI_API_KEY=tu_clave_de_openai
WHATSAPP_TOKEN=tu_token_de_whatsapp
PHONE_NUMBER_ID=tu_id_de_numero_de_telefono
```

## Integración

Para integrar este agente con tu sistema de WhatsApp, importa la función `process_whatsapp_message` desde `agent.whatsapp_agent`.
