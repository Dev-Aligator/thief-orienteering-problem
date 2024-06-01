import os
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from construct_map import construct_map
from run_acoplusplus import run_acoplusplus

# Initialize the main Tkinter window
root = Tk()
root.title("Basic GUI Layout")
root.config(bg="skyblue")
root.geometry("1920x1080")

thop_file_path = None  # Global variable to store the selected ThOP file path

# Create left and right frames
left_frame = Frame(root, width=340, height=int(root.winfo_height() * 0.8), bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(root, width=1580, height=int(root.winfo_height() * 0.8), bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)

# Create a label in the left frame
Label(left_frame, text="Input Controller").grid(row=0, column=0, padx=5, pady=5)

# Load the initial image to be displayed in the right frame
initial_image_path = ".config/ThOP.png"
initial_image = Image.open(initial_image_path)
resized_image = initial_image.resize((1500, 1000), Image.LANCZOS)
new_image = ImageTk.PhotoImage(resized_image)

# Display the initial image in the right frame
main_label = Label(right_frame, image=new_image)
main_label.grid(row=0, column=0, padx=5, pady=5)

# Function to open the file dialog and update the image
def open_file_dialog():
    global thop_file_path
    thop_file_path = filedialog.askopenfilename(
        title="Select a ThOP Instance", 
        initialdir="../acoplusplus_thop/instances/", 
        filetypes=[("ThOP Files", "*.thop"), ("All files", "*.*")]
    )
    if thop_file_path:
        new_image = construct_map(thop_file_path, "output.png", show_solution=False)
        main_label.configure(image=new_image)
        main_label.image = new_image

# Function to run the test instance and update the image with the solution
def run_test_instance():
    global thop_file_path
    if thop_file_path:
        thief_route_solution = run_acoplusplus(thop_file_path)
        new_image = construct_map(thop_file_path, "output.png", thief_route_solution=thief_route_solution, show_solution=True)
        main_label.configure(image=new_image)
        main_label.image = new_image

# Create a toolbar in the left frame
tool_bar = Frame(left_frame, width=200, height=int(left_frame.winfo_height() * 0.8))
tool_bar.grid(row=2, column=0, padx=5, pady=5)

# Button to upload a ThOP instance file
choose_file_btn = Button(
    tool_bar, 
    text="Upload a Instance", 
    bg="green", 
    fg="white", 
    activebackground="#0d6e0b", 
    activeforeground="white", 
    font=("Arial", 12, "bold"), 
    command=open_file_dialog
)
choose_file_btn.pack()

# Button to run the instance and display the solution
run_instance_btn = Button(
    tool_bar, 
    text="Run Instance", 
    bg="green", 
    fg="white", 
    activebackground="#0d6e0b", 
    activeforeground="white", 
    font=("Arial", 12, "bold"), 
    command=run_test_instance
)
run_instance_btn.pack()

# Start the Tkinter main loop
root.mainloop()