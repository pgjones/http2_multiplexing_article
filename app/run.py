import asyncio
from random import choices, random

from quart import jsonify, Quart, render_template, websocket


app = Quart(__name__)


@app.route("/")
async def index():
    return await render_template("index.html")


@app.websocket("/ws")
async def ws():
    await websocket.accept()
    while True:
        await asyncio.sleep(1)
        colour = choices(["red", "blue"])
        await websocket.send(colour[0])


@app.route("/markets/<int:market_id>/")
async def get_market(market_id):
    await asyncio.sleep(0.03)
    return jsonify({"asdfs": "asdfs"})
