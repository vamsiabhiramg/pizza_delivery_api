PIZZA DELIVERY API

This is a REST API for a Pizza delivery service built with FastAPI, SQLAlchemy and PostgreSQL.

ROUTES TO IMPLEMENT

Method | Route | Functionality
--- | --- | ---
*Post* | `/auth/signup/` | **Register new user*
*Post* | `/auth/login/` | **Login user*
*Post* | `/orders/order/` | **Place an order*
*Put* | `/orders/order/update/{order_id}/` | **Update an order*
*Put* | `/orders/order/status/{order_id}/` | **Update order status-Superuser*
*Delete* | `/orders/order/delete/{order_id}/` | **Delete/Remove an order*
*Get* | `/orders/user/orders/` | **Get user's orders*
*Get* | `/orders/orders/` | **List all orders made-Superuser*
*Get* | `/orders/orders/{order_id}/` | **Retrieve an order-Superuser*
*Get* | `/orders/user/order/{order_id}/` | **Get user's specific order*
*Get* | `/docs/` | **View API documentation*




