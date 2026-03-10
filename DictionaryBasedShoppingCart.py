items = {
    0:{
        "brand" : "Apple",
        "type" : "Phone",
        "name" : "Iphone 16 pro max",
        "price" : "$1000"
    },
    1:{
        "brand" : "Apple",
        "type" : "Laptop",
        "name" : "Mac book m4",
        "price" : "$4000"
    }
}

user = []

cartItemCounts = 0


addToCart = input("Do you want to add item to your cart ? (press 'y' for yes) >")

if addToCart == "y" or addToCart == "Y" :
    print(items)
    itemIndex = int(input("Enter a index of item > "))
    if itemIndex < len(items) :
        user.append(items[itemIndex])
        print("Item added successfully!")
    else :
        print("Item not found")


viewOrNot = input("Do you want to view your cart ? (press yes for 'y') > ")

if viewOrNot == "y" or viewOrNot == "Y" :
    print(user)


removeItemOrNot = input("Do you want to remove your cart ? (press yes for 'y') > ")

if removeItemOrNot == "y" or removeItemOrNot == "Y" :
    itemIndex = int(input("Enter a index of item > "))
    if itemIndex < len(user)  :
        del user[itemIndex]
        print("Item removed successfully! here is your updated cart items" , user)
    else :
        print("Item not found")
