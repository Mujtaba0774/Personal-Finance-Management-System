from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class ExpenseCreate(BaseModel):
    amount: float
    description: str
    category: str

class BudgetCreate(BaseModel):
    total_budget: float

class SavingGoalCreate(BaseModel):
    goal_amount: float
