import os
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from construct_map import construct_map, CITIES_COLOR
from run_acoplusplus import run_acoplusplus
from tkinter import ttk
from tkscrolledframe import ScrolledFrame
from utils import load_items_in_cities_data, rgbtohex, get_instance_info
# Initialize the main Tkinter window
root = Tk()

# Set the window title, background color, and size
root.title("ThOP Visualiser")
BACKGROUND_COLOR = "skyblue"
root.config(bg=BACKGROUND_COLOR)
root.geometry("1920x1080")

thop_file_path = None  # Global variable to store the selected ThOP file path
thief_packing_plan = None

# Create left and right frames
left_frame = Frame(root, width=340, bg=BACKGROUND_COLOR)
left_frame.pack(side=LEFT, padx=10, pady=5, fill=Y)

right_frame = Frame(root, width=1580, bg='grey')
right_frame.pack(side=LEFT, padx=5, pady=5)

top_left_frame = Frame(left_frame, width=340, bg='grey')
top_left_frame.pack(padx=5, pady=20, fill=X)

bottom_left_frame = Frame(left_frame, width=340, bg='grey')
bottom_left_frame.pack(padx=5, pady=20, fill=X)

# Create a label in the top left frame
Label(top_left_frame, text="Input Controller").pack(padx=5, pady=5)

# Load the initial image to be displayed in the right frame
initial_image_path = ".config/ThOP.png"
initial_image = Image.open(initial_image_path)
resized_image = initial_image.resize((1500, 1000), Image.LANCZOS)
new_image = ImageTk.PhotoImage(resized_image)

# Display the initial image in the right frame
main_label = Label(right_frame, image=new_image)
main_label.pack(padx=5, pady=5)

log_bar = Frame(right_frame, bg="white")
log_bar.pack(padx=5, pady=5, fill="both")

log_label = Label(log_bar, text="Log", font=("Arial", 12, "bold"), bg="white", fg="black", anchor="w", wraplength=1500)
log_label.pack(padx=30, pady=5, side=LEFT)
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

        log_label_info = get_instance_info(thop_file_path)
        log_label_text = "\t-\t".join(["{}: {}".format(key, log_label_info[key]) for key in log_label_info])
        log_label.config(text=log_label_text)

# Function to run the test instance and update the image with the solution
def run_test_instance():
    global thop_file_path, thief_packing_plan
    if thop_file_path:
        thief_route_solution, thief_packing_plan, log_stats = run_acoplusplus(thop_file_path)
        new_image = construct_map(thop_file_path, "output.png", thief_route_solution=thief_route_solution, show_solution=True)
        main_label.configure(image=new_image)
        main_label.image = new_image
        log_label.config(text="Best Profit: {}\tFound at Time: {}\tFound at iteration: {}".format(log_stats[1], log_stats[3], log_stats[2]))
        for widget in packing_plan_bar.winfo_children():
            widget.destroy()        
        
        items_in_cities = load_items_in_cities_data(thop_file_path, True, thief_packing_plan)
        for index, city in enumerate(thief_route_solution):
            try:
                items_in_cur_city = items_in_cities[city]
            except:
                continue
            city_bg_color = rgbtohex(CITIES_COLOR[city])
            row_bg_color = "white" if index % 2 == 0 else "lightgrey"
            items_in_city = [str(item['index']) for item in items_in_cur_city]
            new_city_items_frame = Frame(packing_plan_bar, width=200, height=100, bg=row_bg_color)
            new_city_items_frame.pack(padx=5, pady=0)
            new_packing_plan_label = Label(new_city_items_frame, text=items_in_city, width=26, anchor="w", wraplength=200, bg=row_bg_color)
            new_packing_plan_label.pack(side=LEFT, padx=0, pady=5)
            # Main city label
            new_city_plan_label = Label(new_city_items_frame, text='', wraplength=200, bg=city_bg_color, width=6, height=2)
            new_city_plan_label.pack(side=RIGHT, padx=5, pady=5)
            
            # Sub-label for the number
            sub_label = Label(new_city_plan_label, text=str(city), bg="white", width=5, height=1)
            sub_label.place(relx=0.5, rely=0.5, anchor=CENTER)
# Create a toolbar in the top left frame
tool_bar = Frame(top_left_frame, width=200, height=int(left_frame.winfo_height() * 0.8))
tool_bar.pack(padx=5, pady=5)

# Button to upload a ThOP instance file
choose_file_btn = Button(
    tool_bar, 
    text="Upload a Instance", 
    width=30,
    height=2,
    bg="green", 
    fg="white", 
    activebackground="#0d6e0b", 
    activeforeground="white", 
    font=("Arial", 12, "bold"), 
    command=open_file_dialog
)
choose_file_btn.pack()

# Add a separator between the buttons
separator = ttk.Separator(tool_bar, orient='horizontal')
separator.pack(fill='x', pady=5)

# Button to run the instance and display the solution
run_instance_btn = Button(
    tool_bar, 
    text="Run Instance", 
    width=30,
    height=2,
    bg="#f58d42", 
    fg="white", 
    activebackground="#bd580f", 
    activeforeground="white", 
    font=("Arial", 12, "bold"), 
    command=run_test_instance
)
run_instance_btn.pack()

# Label for the packing plan
Label(bottom_left_frame, text="Packing Plan").pack(padx=5, pady=5)

sf = ScrolledFrame(bottom_left_frame, width=200, height=900, scrollbars="vertical")
sf.pack( expand=1, fill="both", padx=5, pady=5)

sf.bind_arrow_keys(bottom_left_frame)
sf.bind_scroll_wheel(bottom_left_frame)
packing_plan_bar = sf.display_widget(Frame)

# Start the Tkinter main loop
root.mainloop()
