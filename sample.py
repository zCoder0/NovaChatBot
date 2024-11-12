from MyModel import MyModel

while True:
    model = MyModel()
    text = input("Ask ")
    val = model.predict(text)

    print(val)
