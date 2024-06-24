import tkinter as tk
import time

def get_screen_center(root):
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Calculate the center point
    center_x = screen_width // 2
    center_y = screen_height // 2
    
    return center_x, center_y

def center_window(root, width=300, height=200):
    # Get the center point of the screen
    center_x, center_y = get_screen_center(root)
    
    # Calculate the position to place the window at the center
    x = center_x - (width // 2)
    y = center_y - (height // 2)
    
    # Set the geometry of the window
    root.geometry(f'{width}x{height}+{x}+{y}')

def draw_center_text(canvas, width, height, sentence):
    # Calculate the center of the canvas
    center_x = width // 2
    center_y = height // 2
    
    # Split the sentence into words
    words = sentence.split()
    
    for word in words:
        # Clear the canvas
        canvas.delete("all")
        
        # Draw the current word at the center
        canvas.create_text(center_x, center_y, text=word, fill="red", font=("Helvetica", 16))
        
        # Update the canvas
        canvas.update()
        
        # Pause for a short duration
        time.sleep(0.2)  # Adjust the delay as needed

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Centered Window")
    
    # Dimensions for the window
    window_width = 400
    window_height = 300
    
    # Center the window
    center_window(root, window_width, window_height)
    
    # Create a canvas to draw the text
    canvas = tk.Canvas(root, width=window_width, height=window_height)
    canvas.pack()
    
    # Display the words of the sentence one after the other with a faster speed
    draw_center_text(canvas, window_width, window_height, "Things fall apart book by Chinua Achebe. Turning and turning in the widening gyre the falcon cannot hear the falconer")
    
    root.mainloop()


















