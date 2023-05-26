import customtkinter as ctk

import os


ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')
ctk.set_window_scaling(0.9)
ctk.set_widget_scaling(0.9)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Custom Select Color")
        self.geometry(f"{350}x{700}+{100}+{100}")
        self.resizable(False, False)

        # 0 - red, 1 - green, 2 - blue
        self.color_pimary = [0, 120, 215]
        self.color_border = [0, 102, 204]

        self.color_pimary_hex = f"#{self.color_pimary[0]:02x}{self.color_pimary[1]:02x}{self.color_pimary[2]:02x}"
        self.color_border_hex = f"#{self.color_border[0]:02x}{self.color_border[1]:02x}{self.color_border[2]:02x}"

        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=30, fill="both", expand=True)

        self.label_preview = ctk.CTkLabel(text='Порередній перегляд',
                                               master=self.frame, justify=ctk.LEFT)
        self.label_preview.pack(pady=10, padx=10)

        self.canvas = ctk.CTkCanvas(self.frame, width=200, height=200)
        self.canvas.pack()
        self.rect_id = self.canvas.create_rectangle(15, 15, 185, 185, width=3)
        self.canvas.itemconfig(self.rect_id, outline=self.color_border_hex,
                               fill=self.color_pimary_hex)

        #
        #  COLOR pimary
        #
        self.label_color_pimary = ctk.CTkLabel(text='Колір заповнення',
                                               master=self.frame, justify=ctk.LEFT)
        self.label_color_pimary.pack(pady=10, padx=10)

        # Red pimary
        self.slider_color_pimary_red = ctk.CTkSlider(
            master=self.frame, command=self.callback_pimary_red, from_=0, to=255)
        self.slider_color_pimary_red.pack(pady=10, padx=10)
        self.slider_color_pimary_red.set(self.color_pimary[0])

        # Green pimary
        self.slider_color_pimary_green = ctk.CTkSlider(
            master=self.frame, command=self.callback_pimary_green, from_=0, to=255)
        self.slider_color_pimary_green.pack(pady=0, padx=0)
        self.slider_color_pimary_green.set(self.color_pimary[1])

        # Blue pimary
        self.slider_color_pimary_blue = ctk.CTkSlider(
            master=self.frame, command=self.callback_pimary_blue, from_=0, to=255)
        self.slider_color_pimary_blue.pack(pady=10, padx=10)
        self.slider_color_pimary_blue.set(self.color_pimary[2])

        #
        #  COLOR border
        #
        self.label_color_border = ctk.CTkLabel(text='Колір кордону',
                                               master=self.frame, justify=ctk.LEFT)
        self.label_color_border.pack(pady=10, padx=10)

        # Red border
        self.slider_color_border_red = ctk.CTkSlider(
            master=self.frame, command=self.callback_border_red, from_=0, to=255)
        self.slider_color_border_red.pack(pady=10, padx=10)
        self.slider_color_border_red.set(self.color_border[0])

        # Green border
        self.slider_color_border_green = ctk.CTkSlider(
            master=self.frame, command=self.callback_border_green, from_=0, to=255)
        self.slider_color_border_green.pack(pady=0, padx=0)
        self.slider_color_border_green.set(self.color_border[1])

        # Blue border
        self.slider_color_border_blue = ctk.CTkSlider(
            master=self.frame, command=self.callback_border_blue, from_=0, to=255)
        self.slider_color_border_blue.pack(pady=10, padx=10)
        self.slider_color_border_blue.set(self.color_border[2])

        self.checkbox_autoinstall = ctk.CTkCheckBox(
            text='Автоматичне встановлення', master=self.frame)
        self.checkbox_autoinstall.pack(pady=10, padx=10)

        self.checkbox_reload = ctk.CTkCheckBox(
            text='Перезавантажити ПК', master=self.frame)
        self.checkbox_reload.pack(pady=10, padx=10)

        button_save = ctk.CTkButton(text='Зберегти',
                                    master=self.frame, command=self.save_preferences)
        button_save.pack(pady=10, padx=10)

    def callback_pimary_red(self, value):
        self.color_pimary[0] = round(value)
        self.color_pimary_hex = f"#{self.color_pimary[0]:02x}{self.color_pimary[1]:02x}{self.color_pimary[2]:02x}"
        self.canvas.itemconfig(self.rect_id, outline=self.color_border_hex,
                               fill=self.color_pimary_hex)

    def callback_pimary_green(self, value):
        self.color_pimary[1] = round(value)
        self.color_pimary_hex = f"#{self.color_pimary[0]:02x}{self.color_pimary[1]:02x}{self.color_pimary[2]:02x}"
        self.canvas.itemconfig(self.rect_id, outline=self.color_border_hex,
                               fill=self.color_pimary_hex)

    def callback_pimary_blue(self, value):
        self.color_pimary[2] = round(value)
        self.color_pimary_hex = f"#{self.color_pimary[0]:02x}{self.color_pimary[1]:02x}{self.color_pimary[2]:02x}"
        self.canvas.itemconfig(self.rect_id, outline=self.color_border_hex,
                               fill=self.color_pimary_hex)

    def callback_border_red(self, value):
        self.color_border[0] = round(value)
        self.color_border_hex = f"#{self.color_border[0]:02x}{self.color_border[1]:02x}{self.color_border[2]:02x}"
        self.canvas.itemconfig(self.rect_id, outline=self.color_border_hex,
                               fill=self.color_pimary_hex)

    def callback_border_green(self, value):
        self.color_border[1] = round(value)
        self.color_border_hex = f"#{self.color_border[0]:02x}{self.color_border[1]:02x}{self.color_border[2]:02x}"
        self.canvas.itemconfig(self.rect_id, outline=self.color_border_hex,
                               fill=self.color_pimary_hex)

    def callback_border_blue(self, value):
        self.color_border[2] = round(value)
        self.color_border_hex = f"#{self.color_border[0]:02x}{self.color_border[1]:02x}{self.color_border[2]:02x}"
        self.canvas.itemconfig(self.rect_id, outline=self.color_border_hex,
                               fill=self.color_pimary_hex)

    def save_preferences(self):
        autoinstall = self.checkbox_autoinstall.get()
        reload = self.checkbox_reload.get()

        with open('ChangeSelectColor.reg', 'wb') as f:
            text = f'''Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Control Panel\Colors]
"Hilight"="{self.color_border[0]} {self.color_border[1]} {self.color_border[2]}"
"HotTrackingColor"="{self.color_pimary[0]} {self.color_pimary[1]} {self.color_pimary[2]}"'''
            binary_data = text.encode('utf-8')
            f.write(binary_data)

        if autoinstall:
            os.system('ChangeSelectColor.reg')
            os.remove('ChangeSelectColor.reg')

        if reload:
            os.system("shutdown -t 0 -r -f")


if __name__ == "__main__":
    app = App()
    app.mainloop()
