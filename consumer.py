from products.models import Product
import paho.mqtt.subscribe as subscribe
import json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","app.settings")
django.setup()
def print_msg(client, userdata, message):
    print("%s : %s" % (message.topic, message.payload))
    id = json.loads(message.payload)
    print(data)
    product = Product.objects.get(id=id)
    product.likes = product.likes+1
    product.save()
    print('Product likes increased')
    
print('Started Consuming')
subscribe.callback(print_msg, "/admin", hostname="192.168.0.29",port=1882,auth = {'username':"henda", 'password':"henda"})