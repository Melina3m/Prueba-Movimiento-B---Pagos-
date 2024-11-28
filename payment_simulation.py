import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

# Función de autenticación

def authenticate_user(username, password):
    """Simula la autenticación usando la API de reqres.in."""
    auth_url = "https://reqres.in/api/login"
    auth_data = {'email': username, 'password': password}
    try:
        response = requests.post(auth_url, data=auth_data)
        response.raise_for_status()
        return response.json().get('token')
    except requests.exceptions.RequestException as e:
        print(f"Error en la autenticación: {e}")
        return None

#  Función de procesamiento de pago

def process_payment(token, user_id, amount, sender_account, recipient_account):
    """Simula el procesamiento de un pago."""
    payment_url = "https://jsonplaceholder.typicode.com/posts"
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

    # Crear un número de referencia para la transacción
    transaction_reference = f"REF-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    # Datos de la transacción
    transaction_details = {
        'user_id': user_id,
        'amount': amount,
        'sender_account': sender_account,
        'recipient_account': recipient_account,
        'transaction_reference': transaction_reference,
        'transaction_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    try:
        response = requests.post(payment_url, headers=headers, json=transaction_details)
        response.raise_for_status()

        # Confirmamos que el pago fue procesado
        if response.status_code == 201:
            return transaction_details
        else:
            raise Exception("Error en el procesamiento del pago")
    except requests.exceptions.RequestException as e:
        print(f"Error en el pago: {e}")
        return None

# Datos de prueba

# Datos de autenticación para probar con la API
username = "eve.holt@reqres.in"  # Usa datos válidos de la API reqres.in
password = "cityslicka"
user_id = "12345"
amount = 250
sender_account = "123-456-789"
recipient_account = "987-654-321"

# Autenticación
token = authenticate_user(username, password)

if token:
    print("Autenticación exitosa. Procesando pago...")
    transaction_details = process_payment(token, user_id, amount, sender_account, recipient_account)

    if transaction_details:
        print("Pago realizado con éxito.")
        # Muestra los detalles de la transacción
        print(f"Comprobante de Transacción:")
        print(f"Número de referencia: {transaction_details['transaction_reference']}")
        print(f"Monto: {transaction_details['amount']}")
        print(f"Fecha: {transaction_details['transaction_date']}")
        print(f"Cuenta Remitente: {transaction_details['sender_account']}")
        print(f"Cuenta Destinatario: {transaction_details['recipient_account']}")
    else:
        print("Error al procesar el pago.")
else:
    print("Error en la autenticación.")
