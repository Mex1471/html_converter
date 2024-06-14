import tkinter as tk
from tkinter import filedialog, messagebox
import os
import plistlib
from bs4 import BeautifulSoup

def convert_webarchive_to_html(webarchive_path, output_dir):
    try:
        with open(webarchive_path, 'rb') as f:
            webarchive_data = plistlib.load(f)

        main_resource = webarchive_data.get('WebMainResource', {})
        subresources = webarchive_data.get('WebSubresources', [])

        # Main HTML content
        html_data = main_resource.get('WebResourceData', b'').decode('utf-8')
        soup = BeautifulSoup(html_data, 'html.parser')

        # Insert subresources
        for resource in subresources:
            url = resource.get('WebResourceURL', '')
            data = resource.get('WebResourceData', b'')
            if url and data:
                # Check the type of resource (e.g., images, CSS, JS)
                if url.endswith('.css'):
                    style_tag = soup.new_tag('style')
                    style_tag.string = data.decode('utf-8')
                    soup.head.append(style_tag)
                elif url.endswith('.js'):
                    script_tag = soup.new_tag('script')
                    script_tag.string = data.decode('utf-8')
                    soup.head.append(script_tag)
                else:
                    # If it is an image or other type of resource, handle accordingly
                    pass

        output_file = os.path.join(output_dir, os.path.basename(webarchive_path).replace('.webarchive', '.html'))
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(str(soup))

        return True
    except Exception as e:
        print(f"Error converting {webarchive_path}: {e}")
        return False

def select_files():
    files = filedialog.askopenfilenames(filetypes=[("WebArchive files", "*.webarchive")])
    file_listbox.delete(0, tk.END)
    for file in files:
        file_listbox.insert(tk.END, file)

def select_output_dir():
    dir_path = filedialog.askdirectory()
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(0, dir_path)

def convert_files():
    files = file_listbox.get(0, tk.END)
    output_dir = output_dir_entry.get()
    create_subfolder = create_subfolder_var.get()

    if not files:
        messagebox.showwarning("No files selected", "Please select at least one WebArchive file.")
        return

    if not output_dir:
        messagebox.showwarning("No output directory", "Please select an output directory.")
        return

    if create_subfolder:
        output_dir = os.path.join(output_dir, "html converted")
        os.makedirs(output_dir, exist_ok=True)

    success_count = 0
    for file in files:
        if convert_webarchive_to_html(file, output_dir):
            success_count += 1

    messagebox.showinfo("Conversion complete", f"Successfully converted {success_count} files.")

def set_output_dir_from_file(event):
    if file_listbox.curselection():
        file_path = file_listbox.get(file_listbox.curselection()[0])
        output_dir = os.path.dirname(file_path)
        output_dir_entry.delete(0, tk.END)
        output_dir_entry.insert(0, output_dir)

root = tk.Tk()
root.title("WebArchive to HTML Converter")

file_frame = tk.Frame(root)
file_frame.pack(pady=10)

select_files_button = tk.Button(file_frame, text="Select WebArchive Files", command=select_files)
select_files_button.pack(side=tk.LEFT)

file_listbox = tk.Listbox(file_frame, selectmode=tk.MULTIPLE, width=50)
file_listbox.pack(side=tk.LEFT, padx=10)
file_listbox.bind('<Double-1>', set_output_dir_from_file)

output_dir_frame = tk.Frame(root)
output_dir_frame.pack(pady=10)

output_dir_label = tk.Label(output_dir_frame, text="Output Directory:")
output_dir_label.pack(side=tk.LEFT)

output_dir_entry = tk.Entry(output_dir_frame, width=50)
output_dir_entry.pack(side=tk.LEFT, padx=10)

select_output_dir_button = tk.Button(output_dir_frame, text="Browse", command=select_output_dir)
select_output_dir_button.pack(side=tk.LEFT)

create_subfolder_var = tk.BooleanVar()
create_subfolder_checkbox = tk.Checkbutton(root, text="Create 'html converted' subfolder", variable=create_subfolder_var)
create_subfolder_checkbox.pack(pady=10)

convert_button = tk.Button(root, text="Convert", command=convert_files)
convert_button.pack(pady=20)

root.mainloop()
