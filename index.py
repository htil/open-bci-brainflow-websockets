from physiogo import PhysioGo


def main():
    app = PhysioGo('/dev/cu.usbmodem1', "ganglion")  # create app


if __name__ == "__main__":
    main()
