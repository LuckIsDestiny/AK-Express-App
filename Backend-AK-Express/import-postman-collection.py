import json

# Define the Postman collection as a Python dictionary
postman_collection = {
    "info": {
        "name": "AK Express Backend API",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    },
    "item": [
        {
            "name": "Register - Admin",
            "request": {
                "method": "POST",
                "header": [
                    {"key": "Content-Type", "value": "application/json"}
                ],
                "body": {
                    "mode": "raw",
                    "raw": json.dumps({
                        "name": "Admin One",
                        "email": "admin@akexpress.com",
                        "password": "admin123",
                        "role": "Admin"
                    }, indent=2)
                },
                "url": {
                    "raw": "http://localhost:5000/api/auth/register",
                    "protocol": "http",
                    "host": ["localhost"],
                    "port": "5000",
                    "path": ["api", "auth", "register"]
                }
            }
        },
        {
            "name": "Register - Delivery Boy",
            "request": {
                "method": "POST",
                "header": [
                    {"key": "Content-Type", "value": "application/json"}
                ],
                "body": {
                    "mode": "raw",
                    "raw": json.dumps({
                        "name": "Delivery Guy",
                        "email": "delivery@akexpress.com",
                        "password": "deliver123",
                        "role": "DeliveryBoy"
                    }, indent=2)
                },
                "url": {
                    "raw": "http://localhost:5000/api/auth/register",
                    "protocol": "http",
                    "host": ["localhost"],
                    "port": "5000",
                    "path": ["api", "auth", "register"]
                }
            }
        },
        {
            "name": "Login - Admin",
            "request": {
                "method": "POST",
                "header": [
                    {"key": "Content-Type", "value": "application/json"}
                ],
                "body": {
                    "mode": "raw",
                    "raw": json.dumps({
                        "email": "admin@akexpress.com",
                        "password": "admin123"
                    }, indent=2)
                },
                "url": {
                    "raw": "http://localhost:5000/api/auth/login",
                    "protocol": "http",
                    "host": ["localhost"],
                    "port": "5000",
                    "path": ["api", "auth", "login"]
                }
            }
        }
    ]
}

# Save the JSON to a file
file_path = "ak_express_postman_collection.json"
# Add more endpoints to the Postman collection
additional_endpoints = [
    {
        "name": "Login - Delivery Boy",
        "request": {
            "method": "POST",
            "header": [
                {"key": "Content-Type", "value": "application/json"}
            ],
            "body": {
                "mode": "raw",
                "raw": json.dumps({
                    "email": "delivery@akexpress.com",
                    "password": "deliver123"
                }, indent=2)
            },
            "url": {
                "raw": "http://localhost:5000/api/auth/login",
                "protocol": "http",
                "host": ["localhost"],
                "port": "5000",
                "path": ["api", "auth", "login"]
            }
        }
    },
    {
        "name": "Create Delivery Order (Admin)",
        "request": {
            "method": "POST",
            "header": [
                {"key": "Content-Type", "value": "application/json"},
                {"key": "Authorization", "value": "Bearer {{admin_token}}"}
            ],
            "body": {
                "mode": "raw",
                "raw": json.dumps({
                    "orderId": "ORD1234",
                    "customerName": "Rahul Sharma",
                    "address": "MG Road, Bangalore"
                }, indent=2)
            },
            "url": {
                "raw": "http://localhost:5000/api/delivery/create",
                "protocol": "http",
                "host": ["localhost"],
                "port": "5000",
                "path": ["api", "delivery", "create"]
            }
        }
    },
    {
        "name": "Assign Order to Delivery Boy (Admin)",
        "request": {
            "method": "PUT",
            "header": [
                {"key": "Content-Type", "value": "application/json"},
                {"key": "Authorization", "value": "Bearer {{admin_token}}"}
            ],
            "body": {
                "mode": "raw",
                "raw": json.dumps({
                    "orderId": "ORD1234",
                    "deliveryBoyId": "{{deliveryBoyId}}"
                }, indent=2)
            },
            "url": {
                "raw": "http://localhost:5000/api/delivery/assign",
                "protocol": "http",
                "host": ["localhost"],
                "port": "5000",
                "path": ["api", "delivery", "assign"]
            }
        }
    },
    {
        "name": "Get All Orders (Admin)",
        "request": {
            "method": "GET",
            "header": [
                {"key": "Authorization", "value": "Bearer {{admin_token}}"}
            ],
            "url": {
                "raw": "http://localhost:5000/api/delivery/all",
                "protocol": "http",
                "host": ["localhost"],
                "port": "5000",
                "path": ["api", "delivery", "all"]
            }
        }
    },
    {
        "name": "Get My Orders (DeliveryBoy)",
        "request": {
            "method": "GET",
            "header": [
                {"key": "Authorization", "value": "Bearer {{delivery_token}}"}
            ],
            "url": {
                "raw": "http://localhost:5000/api/delivery/my-orders",
                "protocol": "http",
                "host": ["localhost"],
                "port": "5000",
                "path": ["api", "delivery", "my-orders"]
            }
        }
    },
    {
        "name": "Update Delivery Status (DeliveryBoy)",
        "request": {
            "method": "PUT",
            "header": [
                {"key": "Content-Type", "value": "application/json"},
                {"key": "Authorization", "value": "Bearer {{delivery_token}}"}
            ],
            "body": {
                "mode": "raw",
                "raw": json.dumps({
                    "orderId": "ORD1234",
                    "status": "Delivered"
                }, indent=2)
            },
            "url": {
                "raw": "http://localhost:5000/api/delivery/status",
                "protocol": "http",
                "host": ["localhost"],
                "port": "5000",
                "path": ["api", "delivery", "status"]
            }
        }
    }
]

# Append additional endpoints to the original collection
postman_collection["item"].extend(additional_endpoints)

# Save the updated collection to the same file
with open(file_path, "w") as file:
    json.dump(postman_collection, file, indent=2)

file_path
