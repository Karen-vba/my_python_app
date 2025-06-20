import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("簡單小算盤")

        self.expression = ""
        self.input_text = tk.StringVar()

        # 顯示輸入和結果的視窗
        self.input_frame = tk.Frame(master, width=310, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.input_frame.pack(side=tk.TOP)

        self.input_field = tk.Entry(self.input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10) # 內部填充

        # 按鈕框架
        self.btns_frame = tk.Frame(master, width=310, height=270, bg="grey")
        self.btns_frame.pack()

        # 第一行按鈕 (7, 8, 9, /)
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        # 第二行按鈕 (4, 5, 6, *)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        # 第三行按鈕 (1, 2, 3, -)
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        # 第四行按鈕 (0, C, =, +)
        self.create_button("0", 4, 0)
        self.create_button("C", 4, 1) # 清除
        self.create_button("=", 4, 2) # 等於
        self.create_button("+", 4, 3)

    def create_button(self, text, row, column):
        """建立按鈕並放置到grid佈局中"""
        btn = tk.Button(self.btns_frame, text=text, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.button_click(text))
        btn.grid(row=row, column=column, padx=1, pady=1)

    def button_click(self, item):
        """處理按鈕點擊事件"""
        if item == "C":
            self.expression = ""
            self.input_text.set("")
        elif item == "=":
            try:
                # 使用 eval 函式計算表達式的值
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result # 將結果作為新的表達式起點
            except Exception as e:
                self.input_text.set("錯誤")
                self.expression = ""
        else:
            self.expression += str(item)
            self.input_text.set(self.expression)

# 建立 Tkinter 視窗
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()