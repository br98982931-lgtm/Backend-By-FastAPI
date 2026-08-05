from fastapi import FastAPI, HTTPException, Path, Query
import json

app=FastAPI()

def load_data():
    with open('registrations.json') as f:
        data=json.load(f)
    return data
def save_data(data):
    with open('registrations.json','w') as f:
        json.dump(data,f,indent=4)

@app.get('/view')
def view():
    data=load_data()
    return data

@app.post('/register')
def register_person(person: dict):
    data=load_data()
    data.append(person)
    save_data(data)
    return {"message": "Person registered successfully"}