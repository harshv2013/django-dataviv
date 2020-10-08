import requests
import json

data = {
"image_url": "https://storage.googleapis.com/camerax-bucket/Attendence_data/5b037175f04646b59e911654ba9a9226.jpg?Expires=1602160810&GoogleAccessId=camerax%40brave-computer-288608.iam.gserviceaccount.com&Signature=ECSlF6BFerQu%2F1gAwOM%2F36L%2F4BpIspLbrCXwGzvg0bxTFzBc1U20TshSRnZbTvORLLrRPbXrCYBJXOAcR%2BnPRZ9rsqudYntP1bBmE55YCOMvtsR%2F3hSpFT55JVgTuUkzRfkcXNqK4SLLiuPpqBQxPhtola92eQAAIsrel7mLE0dzfM3%2FCl3TUrj2KQTE6JuQ55tTnqBulRxD3O5zu6K2IXMkyTP0sVkH3XlIiUgVhnETMKurnF%2FY487hEaMZuYHh%2Fkdq2dZO3ODhUgDOMf3cRms2oi16DtMgV3%2FKFwrjUZmgVUtgafzuy5USxqO13UwJ5MtW5F9q5nR%2FtFXUHW0hIw%3D%3D",
"bound":[442, 802, 1173, 72],
"store_id":9
}

data = json.dumps(data)

print('data -----',data)
headers = {"Authorization": "Token 12f720476f74a93fab1f119e5286c355c348fd64", "Content-Type":"application/json"}
r = requests.post(url='http://34.122.179.12:8000/camera/attendence/', data = data, headers=headers)
print(r.__dict__)