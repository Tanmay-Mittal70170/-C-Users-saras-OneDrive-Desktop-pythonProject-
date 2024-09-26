import tkinter
import customtkinter
import messagebox
import datetime
from PIL import Image,ImageTk

# Initialize the main application window
s = customtkinter.CTk()
s.geometry("800x500")  # Set the window size
s.configure(fg_color="#E0E0E0")  # Configure background color

image = Image.open(R"C:\Users\saras\OneDrive\Desktop\resource\pngtree-light-green-branches-and-leaves-watermark-floral-plant-background-image_736510.jpg")

# Define the new size
new_size = (800,500)  # Set your desired width and height

# Resize the image using a specific resampling filter
resized_image = image.resize((800,500), resample=Image.LANCZOS)

# Create a CTkImage from the resized image
ctk_image = customtkinter.CTkImage(resized_image)

# Now you can use this CTkImage in CTkLabel
label = customtkinter.CTkLabel(s, image=ctk_image)  # 's' is your customtkinter window
label.place(x=0, y=0)  # Place the label where desired


# Create labels for username and password fields
label = customtkinter.CTkLabel(s, text="Username", font=("Arial", 30), text_color="#003366")
label.place(x=200, y=100)

label2 = customtkinter.CTkLabel(s, text="Password", font=("Arial", 30), text_color="#003366")
label2.place(x=200, y=200)

# Create entry fields for user input
text = customtkinter.CTkEntry(s, placeholder_text="Enter your userid", width=250, height=40)
text.place(x=450, y=100)

text2 = customtkinter.CTkEntry(s, placeholder_text="Enter the password", show="*", width=250, height=40)
text2.place(x=450, y=200)

# Function to change the color of the login button when clicked
def change_color():
    global buttonc
    # Toggle button color between Deep Sky Blue and Tomato
    if buttonc == "#00BFFF":  # Deep Sky Blue
        buttonc = "#FF6347"  # Tomato color
    else:
        buttonc = "#00BFFF"  # Deep Sky Blue
    button.configure(fg_color=buttonc)

# Create the login button
button = customtkinter.CTkButton(s, text="LOGIN", text_color="#FFFFFF", font=("Arial", 20), corner_radius=15, width=150, height=40,
                                 command=change_color, fg_color="#00BFFF")
button.configure(fg_color="#4682B4")
button.place(x=350, y=300)
buttonc = "#4682B4"

# Function to store the username and login time in a text file
def store():
    f = open(R"C:\Users\saras\OneDrive\Desktop\New Text Document (2).txt", "a")  # Open file for appending
    now = datetime.datetime.now()  # Get the current date and time
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Format the current time
    if text2.get() == "tanmay@123":  # Check if the password is correct
        # Write the username and login time to the file
        f.write(f"Username: {text.get()}, Logged in at: {formatted_time}\n")
    f.close()  # Close the file

# Function to clear the input fields and display success or error messages
def clear():
    if not text.get():  # Check if the username field is empty
        messagebox.showerror("ERROR", "Enter the Username")  # Show error message
        return  # Exit the function
    if text2.get() == "tanmay@123":  # Check if the password is correct
        messagebox.showinfo("Welcome", "You successfully completed the login")  # Show success message
        # Destroy the input fields and labels to clear the screen
        text.destroy()
        text2.destroy()
        label.destroy()
        label2.destroy()
        button.destroy()
    else:
        messagebox.showerror("Error", "Invalid Password")  # Show error message for invalid password

# Configure the button to execute functions upon clicking
button.configure(command=lambda: [change_color(), store(), clear()])

# Start the main loop to run the application
s.mainloop()
