from flask import Blueprint

__author__ = 'jushitaa'


item_blueprint = Blueprint('/items', __name__)


@item_blueprint.route('/item/<string:name>')
def item_page(name):
    pass


@item_blueprint.route('/load')
def load_item():
    """

    Loads an item's data using store's data aand return a JSON representation
    :return:
    """
    pass