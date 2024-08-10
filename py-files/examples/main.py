from fastapi import FastAPI
from enum import Enum
from typing import Optional 


app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Hello World"}



@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}



@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}



class ModelName(str, Enum):
    ALEXNET = "ALEXNET"
    RESNET = "RESNET"
    LENET = "LENET"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.ALEXNET:
        return {"model_name": model_name}
    elif model_name == "LENET":
        return {"model_name": model_name}
    elif model_name == ModelName.RESNET:
        return {"model_name": model_name}
    else:
        return {"model_name": model_name, "message": "Not found"}
    



dummy_db = [{"item_name": "t-shirt"}, {"item_name": "shoe"}, {"item_name": "watch"}]
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10, optional_parameter: Optional[int] = None):
    return {"items": dummy_db[skip:skip+limit], "optional_parameter": optional_parameter}

#http://127.0.0.1:8000/items/?skip=0&limit=1&optional_parameter=123456




@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: int, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})

    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )

    return item
"""
http://127.0.0.1:8000/users/1/items/2?q=gurkan_albayrak

{
  "item_id": 2,
  "owner_id": 1,
  "q": "gurkan_albayrak",
  "description": "This is an amazing item that has a long description"
}

"""








#1
"""
...../items/1
...../items/2    her biri yeni bir sayfa, items ın altında olacak tabi. 
...../items/3   

"""
"""
pydentic bir veri doğrulama kütüphanesidir. 
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    quantity: int = 0  # Varsayılan değer

# Geçerli veri ile model oluşturma
item = Item(name="Elma", price=2.5)

# Geçersiz veri ile model oluşturma (hata verir)
invalid_item = Item(name="Armut", price="ucuz")

"""



#2
"""
mypy,

 Python kodunda statik tip denetimi yapmak için kullanılan bir araçtır. 
 Python, dinamik olarak tip tanımlayan bir dil olmasına rağmen, mypy gibi araçlar sayesinde kodunuza 
 statik tip açıklamaları ekleyebilir ve bu açıklamaların doğru olup olmadığını kontrol edebilirsiniz. 
 Bu, özellikle büyük kod tabanlarında ve ekip çalişmalarında hataları erken yakalamaya ve kodun daha 
 güvenilir olmasına yardımcı olur.

mypy Kullanımının Ana Faydaları:
Tip Hatalarını Erken Yakalama: mypy, kodunuz çalıştırılmadan önce olası tip hatalarını bulmanızı sağlar.
 Örneğin, bir fonksiyona bir int beklerken yanlışlıkla bir str gönderiyorsanız, mypy bu hatayı size bildirir.

Kodun Anlaşılabilirliğini Artırma: Tip açıklamaları, kodun ne yaptığını anlamayı kolaylaştırır. Kodunuzu 
okuyan diğer geliştiriciler, hangi türlerde veri beklediğinizi ve döndürdüğünüzü hemen görebilirler.

IDE ve Araç Desteği: Birçok IDE, mypy ile entegre çalışır ve kod yazarken size anında geri bildirim sağlar.
 Bu, geliştirici deneyimini iyileştirir ve hataları erken tespit etmenizi sağlar.

Statik Analiz: mypy, Python kodunuzu çalıştırmadan analiz eder, bu da büyük projelerde ve sürekli entegrasyon
 süreçlerinde faydalıdır.

Örnek Kullanım:
python
Kodu kopyala
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Hata: greet fonksiyonu bir str bekliyor, ama int verilmiş
result = greet(123)
"""






#3
"""
from enum import Enum
Neden Kullanılır?
Okunabilirlik: Anlamlı isimler, kodun ne yaptığını daha açık hale getirir.
Hata Azaltma: Sabit değerler yerine Enum kullanmak, yanlış değerlerin kullanılmasını önler.
Grup Sabitler: Benzer özelliklere sahip sabitleri bir araya getirir.
Örnek Kullanım:
python
Kodu kopyala
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Enum üyelerine erişim
print(Color.RED)
print(Color.GREEN.name)  # Üyenin ismini alır
print(Color.BLUE.value)  # Üyenin değerini alır
"""