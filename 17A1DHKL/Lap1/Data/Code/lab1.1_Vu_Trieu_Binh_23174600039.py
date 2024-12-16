import xml.etree.ElementTree as ET

class XMLReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def  read_xml(self):
        tree = ET.parse(self.file_path)
        self.data = tree.getroot()


    def display_data(self):
        if self.data:
            for product in self.data.findall('product'):
                name = product.find('name').text
                price = product.find('price').text
                quantity = product.find('quantity').text
                print(f"Product: {name}, Price : {price}, Quantity: {quantity}")
    
#sử dụng lớp XMLReader 
path = 'Lap1/Data/products.xml'
reader = XMLReader(path)
reader.read_xml()
reader.display_data()
