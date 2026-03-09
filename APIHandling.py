import requests


def getProducts () :
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    data = response.json()

    if data:
        return data[0]["title"]
    else :
        raise Exception("Faild to fetch product data")
    


def main () :
    try :
       productData = getProducts()
       print(productData)
    except Exception as e :
        print(str(e))


if __name__ == "__main__" :
    main()
