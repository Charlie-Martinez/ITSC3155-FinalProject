from . import orders, order_details, customers, payments, promotions, ratings, sandwiches, recipes, resources


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(customers.router)
    app.include_router(payments.router)
    app.include_router(promotions.router)
    app.include_router(ratings.router)
    app.include_router(sandwiches.router)
    app.include_router(recipes.router)
    app.include_router(resources.router)
