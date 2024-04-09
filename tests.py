import pytest
import requests

#CRUD 
BASE_URL = 'http://127.0.0.1:5000'
tasks = []

# create a new task test
def test_create_task():
    new_task_data={
      "title": "New task",
      "description": "New task description", 
      "completed": False
    }
    
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 201
    
    response_json = response.json()
    assert "id" in response_json
    assert "message" in response_json
    tasks.append(response_json['id'])
    
# get all tasks test
def test_get_tasks():
  response = requests.get(f"{BASE_URL}/tasks")
  assert response.status_code == 200
  assert "tasks" in response.json()
  
# get task by id test
def test_get_task_by_id():
  if tasks:
    task_id = tasks[0]
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert task_id == response_json["id"]

# update a task test    
def test_update_task():
  if tasks:
    task_id = tasks[0]
    payload={
      "title": "Updated task",
      "description": "Updated task description", 
      "completed": True
      }

    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
    assert response.status_code == 200
    
    response_json = response.json()
    assert response_json["title"] == payload["title"]
    assert response_json["description"] == payload["description"]
    assert response_json["completed"] == payload["completed"]
    
# update a task test    
def test_delete_task():
  if tasks:
    task_id = tasks[0]

    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    
    response_json = response.json()
    assert "id" in response_json