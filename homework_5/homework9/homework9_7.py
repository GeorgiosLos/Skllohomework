import xml.etree.ElementTree as ET

def main():
    
    tree = ET.parse("/home/hp/Skillohomework/homework_5/homework9/inventory.xml")
    root = tree.getroot()
    
    
    for product in root.findall("product"):
        name = product.find("name").text
        price = float(product.find("price").text)
        
        print(f"Name: {name}, Price: ${price}")

if __name__ == "__main__":
    main()
