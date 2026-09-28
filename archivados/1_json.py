import json

# Estructura de datos básica para una cuenta de Mercado Pago
cuenta_mercado_pago = {
    "user_id": 123456789,
    "personal_info": {
        "first_name": "Juan",
        "last_name": "Pérez",
        "email": "juan.perez@email.com",
        "phone": "+5491112345678",
        "identification": {
            "type": "DNI",
            "number": "38123456"
        }
    },
    "account_status": "active",
    "wallet": {
        "balance": 15450.50,
        "currency": "ARS",
        "cvu": "0000003100012345678901",
        "alias": "juan.perez.mp"
    },
    "payment_methods": [
        {
            "id": "card_98765",
            "type": "credit_card",
            "issuer": "Visa",
            "last_four_digits": "4321",
            "is_default": True
        },
        {
            "id": "card_54321",
            "type": "debit_card",
            "issuer": "Mastercard",
            "last_four_digits": "8765",
            "is_default": False
            
        }
    ],
    "investments": {
        "invested_balance": 50000.00,
        "yield_percentage": 72.5,
        "auto_invest_enabled": True
    }
}

json_data = json.dumps(cuenta_mercado_pago, indent=4, ensure_ascii=False)

print(json_data)