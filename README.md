# TheTeam_Queue
REST service for University of Colorado's Data Engineering Course, Spring 2015

## Description
This service will use Flask, Python, and SQLite to enqueue and dequeue students who are waiting for assistance from a Learning Assistant.

###### Teammembers
- Justin McBride: dare599z
- Tyler Bussell: TylerBussell
- Alexia Newgord: alne4294
- David: driabwb

#### Data Contents
* Name 
* Time Submitted
* Course
* If Helped
* Location
* Duration
* HelpedBy

#### Requests
| GET | DELETE | POST | PUT | Prefix |
| --- | ------ | ---- | --- | ------ | 
| /queue | /remove/id/# | /enqueue | /modify/id/# | /api/1.0 |
| /queue/id/# | | | /dequeue/id/#
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
"subTime":dateTime,
"course":string,
"helped":bool,
"location":string,
"duration":int,
"helpedBy":string
"eid":string}
```

#### Request Examples
_Python/Flask_

Example GET Request (note: defaults to get):
```python
@app.route('/api/1.0/queue/pos/<int:x>')
def getPos(x):
  findInDatabase(x)
    return format_response(true/false, x)
    
def format_response(bool, obj)
  return <data_object>
```

Example PUSH Request:
```python
@app.route('url',methods=['PUSH'])
```

To get posted object:
```python
y = request.json
```

#### Queue API
```
entryList.add(entry), boolean
         .modify(entry), object
         .remove(entry), boolean
         .getById(<id>), object
         .getByPos(<position>), object
         .getAll(), queue
```
