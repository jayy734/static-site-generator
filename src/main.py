from textnode import TextNode

def main():
    node1 = TextNode("Hello, world!", "bold", "https://example.com")
    node2 = TextNode("Hello, world!", "bold", "https://example.com")
    print(node1 == node2)  # True
    print(repr(node1))
          
        
if __name__ == "__main__":
    main()