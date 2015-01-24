# TheTeam_Queue
REST service for University of Colorado's Data Engineering Course, Spring 2015

## Description
This service will enqueue and dequeue students who are waiting for assistance from a Learning Assistant.

#### Data contents
| Name | Time Submitted | Class | If Helped | Location | Duration |

#### Requests
| GET | DELETE | POST | PUT | Prefix |
| --- | ------ | ---- | --- | ------ | 
| /queue | /remove/io/# | /enqueue | /modify/id/#
| /queue/id/# | | /dequeue/id#
| /queue/pos/# | 
