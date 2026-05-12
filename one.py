def Hello(n):
    return n.lower()


def main():
    a = input("Enter in uppercase: ")
    whisper = Hello(a)
    print(f"Speak quietly -- {whisper}")

if __name__ == "__main__":
    main()