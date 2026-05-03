from . import orders, order_details, customers, payments, promotions, ratings, sandwiches, resources, recipes

from ..dependencies.database import engine


def index():
    customers.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    payments.Base.metadata.create_all(engine)
    ratings.Base.metadata.create_all(engine)