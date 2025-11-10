from django.shortcuts import redirect, render

products=[
    {
        'id':1,
        'name':'jagan',
        'age': 22
     },
     {
        'id':2,
        'name':'shekar',
        'age':20
     },
     {
        'id':3,
        'name':'ganesh',
        'age': 22
     }
]

def product_view(req):
    if req.method == 'POST':
        input_name = req.POST.get('name')
        input_age = req.POST.get('age')
        id = len(products) + 1
        new_prod = {
            'id' : id,
            'name' : input_name,
            'age' : input_age

       }
        products.append(new_prod)
    return render(req,'index.html', {'products':products})


def delete_product(req, id):
    global products
    new_product=[]
    for prod in products:
        if prod.get('id') != id:
            new_product.append(prod)
    products = new_product
    return redirect('/')


def update_product(req, id):

    if req.method == 'POST':
        new_name = req.POST.get('name')
        new_age = req.POST.get('age')

        global products
        for prob in products:
            if prob.get('id') == id:
                prob['name'] = new_name
                prob['age'] = new_age
                break
        return render(req, "index.html", {'products': products})   

    requred_product = None
    for prod in products:
        if prod.get('id') == id:
            requred_product = prod
            break
    return render(req, 'edit.html', requred_product)