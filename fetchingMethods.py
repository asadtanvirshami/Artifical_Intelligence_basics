import requests

url_get = 'https://six-capable-devourer.glitch.me/user/getAllAgents'
url_post = 'https://six-capable-devourer.glitch.me/tasks/createTask'
url_delete = 'https://six-capable-devourer.glitch.me/tasks/deleteTask'

#GET req
r = requests.get(url=url_get)
r.status_code:200
r.request.headers

#GET req with headers
payload = {'id':'52fb0f11-57ea-486c-8970-b84ef90279b2'}
# r = requests.get(url=url_get, headers=payload)

#GET req with headers
payload = {'id':'52fb0f11-57ea-486c-8970-b84ef90279b2'}
# r = requests.get(url=url_get, headers=payload)

#POST req with body
payload = {
    "title": "Task Title",
    "description": "Task Description",
    "priority": "High", 
    "deadline": "2023-07-31T23:59:59", 
    "startTime": "09:00:00",  
    "startDate": "2023-07-25", 
    "bonus": 1000,  
    "userId": "063cfbc0-0c1f-47f2-9a31-d6325eba0cf4",  
    "companyId": "52fb0f11-57ea-486c-8970-b84ef90279b2" 
}
# r = requests.post(url=url_post, data=payload)

#DELETE req with body
payload = {
    "id": "af08c546-8330-4aa9-8f75-cdb090fca5de",
}
# r = requests.delete(url=url_delete, headers=payload)