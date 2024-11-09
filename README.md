# Location Distance API - Microservices

## Project Description

The **Location Distance API** provides services to calculate the distance between given locations. Users can submit a list of location IDs, and the API will calculate the total distance between them asynchronously using Celery. This API is designed to be used in geolocation systems, map applications, or any platform that requires calculating distances between geographic points.

## Technologies Used

- **Programming Language**: Python
- **Framework**: Django
- **Libraries**:
- Celery (for handling asynchronous tasks)
- Django Rest Framework (for building APIs)
- Math (for mathematical operations and distance calculation)
- AsyncResult (for querying the status of Celery tasks)
- **Data Format**: JSON
- **Database**: Relational database with `Location` model
- **Containerization**: Docker (for packaging and deploying the application in a consistent environment)

## Endpoints

### 1. Calculate Distance

**Method**: POST  
**Path**: `/calculate-distance`  
**Description**: Calculates the total distance between the locations provided in the request. The task is processed asynchronously using Celery.

**Sample request**:

```json
{
    "location_ids": [1, 2, 3]
}
```

**Response example**:

```json
{
    "task_id": "a1b2c3d4e5f6g7h8i9j0",
    "status": "Tarea en proceso"
}

```

### 2. Query Task Status

**Method**: GET
**Path**: `/task-status/{task_id}`
**Description**: Query the status of the asynchronous task specified by task_id

**Request Example**: GET /task-status/a1b2c3d4e5f6g7h8i9j0

**Response Example**:

```json
{
    "task_id": "a1b2c3d4e5f6g7h8i9j0",
    "status": "Success Task",
    "result": {
        "total_distance": 45.67
    }
}

```

### 3. Create locations

**Method**: POST
**Path**: `/create-location`
**Description**: Allows you to create a new location in the database, with latitude and longitude coordinates. This information will be stored to be used in distance calculations.

**Request example**:

```json
{
    "name": "Locations A",
    "latitude": 40.7128,
    "longitude": -74.0060
}

```
**Response example**:

```json
{
    "message": "Locations create success",
    "location_id": 1
}

```

