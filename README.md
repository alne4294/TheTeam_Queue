# TheTeam_Queue
REST service for University of Colorado's Data Engineering Course, Spring 2015

## Description
This service will use Flask, Python, and SQLite to enqueue and dequeue students who are waiting for assistance from a Learning Assistant.

#### Data Contents
* Name 
* Time Submitted
* Class
* If Helped
* Location
* Duration
* HelpedBy

#### Requests
| GET | DELETE | POST | PUT | Prefix |
| --- | ------ | ---- | --- | ------ | 
| /queue | /remove/io/# | /enqueue | /modify/id/# | /api/1.0 |
| /queue/id/# | | /dequeue/id#
| /queue/pos/# | 

#### Returns
```
{"error":"true/false"
"data":errorString/object}
```

#### Data Format
JSON

Class named Entry:
```
{"name":string,
"time_submitted":dateTime,
"class":string,
"helped":bool,
"location":string,
"duration":int,
"helpedBy":string}
```

#### Request Examples
Python/Flask

Example GET Request:
```python
@app.route('/api/1.0/queue/pos/<int:x>')
def getPos(x):
  findInDatabase(x)
    return format(true/false, x)
    
def format(bool, obj)
  return <data_object>
```
