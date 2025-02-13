def kwargsAcceptFun(**kwargs):
    print("Received kwargs:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

kwargsAcceptFun(name="Shoxrux", age=18, department="Cybersecurity")
