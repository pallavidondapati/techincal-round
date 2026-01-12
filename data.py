import requests
import matplotlib.pyplot as plt

api_url="https://69648608e8ce952ce1f1f08f.mockapi.io/students/score"
response=requests.get(api_url)
print("status",response.status_code)
students=response.json()
names=[]
scores=[]
for d in students:
    score=d.get("score")
    name=d.get("name")
    if score is not None:
        scores.append(score)
        names.append(name)
avg_score=sum(scores)/len(scores)
print(avg_score)
plt.bar(names,scores)
plt.bar(names, scores)
plt.axhline(avg_score, linestyle='--', label="Average")
plt.legend()
plt.show()