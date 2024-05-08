import pyqrcode  #pip install pyqrcode
import png  #pip install pypng
import cv2  #pip install opencv-python
import os


#Creates a specified number of spots based on numOfSpots, within the lotName
def createQRCode(lotName: str, numOfSpots: int):
    #Makes a new file to store QR codes if not existed yet
    if not os.path.exists(f"Lot {lotName} QR Codes"):
        os.mkdir(f"Lot {lotName} QR Codes")

    for i in range(1, numOfSpots + 1):
        spotName = f"{lotName}_{i}"
        #Creates a QR code PNG in the specified file
        pyqrcode.create(spotName).png(os.path.join(f"Lot {lotName} QR Codes", spotName + ".png"), scale=10)
#End createQRCode


#Activates the camera and detects and decocdes QR codes shown to camera
def captureVideo():
    detector = cv2.QRCodeDetector()
    # Create video capture feed
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        # Capture each frame of video
        _, frame = cap.read()
        # Show each frame of video
        cv2.imshow('Video', frame)

        # Detect qr code
        # data is an array with the stored QR codes decoded
        _, data, _, _ = detector.detectAndDecodeMulti(frame)

        #Check if the QR code spots are found in each frame of video
        checkForQRCode("B", 10, data)
        #-----This is where you add more checkForQRCode functions-----

        #-------------------------------------------------------------

        # Check for key press to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cap.destroyAllWindows()
# End captureVideo()


# Condition checks if the lotName and spots exist in the decoded data frame
def checkForQRCode(lotName: str, numOfSpots: int, data: []):
    # Checks if any of the QR codes in lotName in range of numOfSpots are in frame
    for i in range(1, numOfSpots + 1):
        spotName = f"{lotName}_{i}"
        # Just prints the results
        print(f"Lot {lotName} Spot {i}:\t{spotName in data}")
#End checkForQRCode()


def main():
    # print("Creating QR Codes")
    # createQRCode("A", 10)
    # print("QR Codes successfully created")

    print("Capturing Video...")
    #Edit this function if you want to check for more QR codes in frame
    captureVideo()
# hi

main()
