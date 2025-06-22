from fastapi import FastAPI, HTTPException
from db import load_data

app = FastAPI()
df = load_data()

@app.get("/banks")
def get_all_banks():
    return df["bank_name"].unique().tolist()

@app.get("/branches/{bank_name}")
def get_branches(bank_name: str):
    filtered = df[df["bank_name"].str.lower() == bank_name.lower()]
    if filtered.empty:
        raise HTTPException(status_code=404, detail="Bank not found")
    return filtered.to_dict(orient="records")
