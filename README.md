# Task API - Flask

API made to help you control tasks in your routine!

## Functionalities

- Create a new task
- Search tasks, edit or delete any of them.
- Tests

## Technologies Used

- Python
- SQLAlchemy
- Flask
- Pytest

## Installing the Project

```
git clone *projet-url*

cd *projects-directory*

pip3 install -r requirements.txt
```

## Routes

### Tasks Routes

#### Create Task

```http
  POST /tasks
```

| Body Data   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `title` | `string` | **Mandatory**. Tasks's title |
| `description` | `string` | **Mandatory**. Tasks's description. |
| `completed` | `boolean` | **Mandatory**. Check to see if task is completed. |

#### Fetch Tasks

```http
  GET /tasks
```


#### Fetch Task by ID

```http
  GET /tasks/:id
```

| Param Data   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `integer` | **Mandatory**. Tasks's ID. |

#### Edit Task

```http
  PUT /tasks/:id
```

| Param Data   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `integer` | **Mandatory**. Tasks's ID. |


| Body Data   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `title` | `string` | **Optional**. Tasks's title |
| `description` | `string` | **Optional**. Tasks's description. |
| `completed` | `boolean` | **Optional**. Check to see if task is completed. |


#### Delete a Meal

```http
  DELETE /tasks/:id
```

| Param Data   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `integer` | **Mandatory**. Tasks's ID. |
