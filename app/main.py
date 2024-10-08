from fastapi import FastAPI, Depends
from .auth import get_current_user
from .routers import expenses, budgets, savings
from .plaid_integration import get_bank_transactions

app = FastAPI()

# Routers for various features
app.include_router(expenses.router)
app.include_router(budgets.router)
app.include_router(savings.router)

# Home route
@app.get("/")
def read_root():
    return {"message": "Personal Finance Management System is up!"}

# Plaid usage route
@app.get("/transactions")
def fetch_transactions(current_user: str = Depends(get_current_user)):
    return get_bank_transactions()
