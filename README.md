# TheTeam_Queue
_REST service for University of Colorado's Data Engineering Course, Spring 2015_

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
| /queue | /remove/id/# | /enqueue | /modify/id/# | /api/1.0 |
| /queue/id/# | | /dequeue/id#
| /queue/pos/# | 

#### Returns
```
{"error":"true/false"
"data":errorString/object}
```

#### Data Format
_JSON_

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
_Python/Flask_

Example GET Request (note: defaults to get):
```python
@app.route('/api/1.0/queue/pos/<int:x>')
def getPos(x):
  findInDatabase(x)
    return format(true/false, x)
    
def format(bool, obj)
  return <data_object>
```

Example PUSH Request:
```python
@app.route('url',methods=['PUSH'])
```
