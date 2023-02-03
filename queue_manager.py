from pydantic import BaseModel
import timer

class Customer(BaseModel):
    name: str
    queue_number: int
    missed_call: int
    
counter = {1: 100, 2: 200, 3: 300, 4: 400, 5: 500}

customer_queue: list = []

served_customers: list = []

    
def register_customer(name: str):
    counter_with_shortest_queue = (0, counter[0])
    for key, value in counter.items():
        if value % 100 < counter_with_shortest_queue:
            counter_with_shortest_queue = (key, value)
    customer = Customer(name=name, queue_number=counter_with_shortest_queue[1])
    customer_queue.append(customer)
    
def call_customer():
    if len(customer_queue) == 0:
        print("The queue is empty.")
    else:
        customer = customer_queue[0]
        customer_queue.pop(0)
        served_customers.append(customer)
    
def list_customer():
