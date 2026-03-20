"""
This is an exemplary project which I use to test the functionality of GitHub.
So that the project makes some sense, I will use it to test the functionality 
of a GUI automation library called PyAutoGUI.
"""

def main():

    import pyautogui, time

    # Get the screen width and height
    screen_width, screen_height = pyautogui.size()

    # Calculate the center coordinates
    center_x = screen_width / 2
    center_y = screen_height / 2

    # Calculate the quartile coordinates
    quartile_x = screen_width / 4
    quartile_y = screen_height / 4

    while True:

        # Move to the center and click
        pyautogui.click(center_x, center_y)

        # Move to the quartile and click
        pyautogui.click(quartile_x, quartile_y) 

        # Wait for 20 seconds with a countdown
        for i in range(20, 0, -1):
            print(f"Waiting... {i}s remaining", end="\r") # end="\r" to overwrite the same line
            time.sleep(1)
        print("Timer complete!")   

if __name__ == "__main__":
    main()