from flask_cors import CORS
from peewee import JOIN, fn

from models import forecast_db, recipes_db, Ingredients, MealkitIngredient, Mealkit, Menu
from flask import Flask, jsonify

# Complete me :)

app = Flask(__name__)
CORS(app)


@app.route('/')
def main():
    return jsonify("Hello World")


@app.route('/getIngredients')
def query():
    ingredients = []
    getQuery = (Ingredients
                .select(Ingredients.name, Ingredients.price, MealkitIngredient.sku_id.alias('sku_id'),
                        fn.SUM(MealkitIngredient.qty_needed).alias('volume'))
                .join(MealkitIngredient)
                .join(Mealkit)
                .join(Menu)
                .group_by(MealkitIngredient.sku_id)
                )

    for ingredient_dict in getQuery.dicts():
        ingredients.append(ingredient_dict)

    return jsonify(ingredients)


if __name__ == "__main__":
    app.run(debug=True)

