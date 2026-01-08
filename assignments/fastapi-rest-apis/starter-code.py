from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="API de Exemplo - FastAPI")


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


items: dict[int, Item] = {}


@app.post("/items/", response_model=Item, status_code=201)
def create_item(item: Item):
    if item.id in items:
        raise HTTPException(status_code=400, detail="Item já existe")
    items[item.id] = item
    return item


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: Item):
    if item_id != updated.id:
        raise HTTPException(status_code=400, detail="IDs incompatíveis")
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    items[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    del items[item_id]
    return None
