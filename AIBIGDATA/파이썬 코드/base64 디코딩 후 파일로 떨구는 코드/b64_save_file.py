import base64

with open('test.txt', 'r') as f:
    data = f.read()

data = data + '=' * (4-len(data) %4)

encoded = data.encode('utf-8')
with open('test.exe', 'wb') as file:
    decoded_data = base64.decodebytes(encoded)
    file.write(decoded_data)
