import sys

def main():
    if len(sys.argv) > 1:
        print(f"Hello, {sys.argv[1]}!")
    else:
        print("Hello, World!")

if __name__ == "__main__":
    main()
