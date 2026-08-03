import tkinter as tk

BG = "#050816"
DISPLAY_BG = "#0b1026"
DISPLAY_FG = "#00f5ff"
SUBTEXT_FG = "#9d4edd"

BTN_NUM_BG = "#10162f"
BTN_NUM_FG = "#ffffff"
BTN_OP_BG = "#3a0ca3"
BTN_OP_FG = "#ffffff"
BTN_EQ_BG = "#ff006e"
BTN_EQ_FG = "#ffffff"
BTN_CLR_BG = "#240046"
BTN_CLR_FG = "#ffbe0b"

HOVER_DARK = "#00bbf9"
HOVER_OP = "#7209b7"
HOVER_EQ = "#ff4d8d"
HOVER_CLR = "#5a189a"

FONT_MAIN = ("Segoe UI", 30, "bold")
FONT_SUB = ("Segoe UI", 13)
FONT_BTN = ("Segoe UI", 18, "bold")
FONT_BTN_SM = ("Segoe UI", 15, "bold")


class NeonCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Neon Calculator")
        self.resizable(False, False)
        self.configure(bg=BG)

        self._expr = ""
        self._result = ""
        self._new_num = False

        self._build_display()
        self._build_buttons()

    def _build_display(self):
        frame = tk.Frame(
            self,
            bg=DISPLAY_BG,
            padx=20,
            pady=18,
            highlightthickness=2,
            highlightbackground="#00f5ff"
        )
        frame.pack(fill="x", padx=14, pady=(18, 8))

        self._sub_var = tk.StringVar(value="")
        tk.Label(
            frame,
            textvariable=self._sub_var,
            bg=DISPLAY_BG,
            fg=SUBTEXT_FG,
            font=FONT_SUB,
            anchor="e"
        ).pack(fill="x")

        self._main_var = tk.StringVar(value="0")
        tk.Label(
            frame,
            textvariable=self._main_var,
            bg=DISPLAY_BG,
            fg=DISPLAY_FG,
            font=FONT_MAIN,
            anchor="e",
            wraplength=330
        ).pack(fill="x")

    def _build_buttons(self):
        grid = tk.Frame(self, bg=BG)
        grid.pack(padx=14, pady=(8, 18))

        layout = [
            [("C", "clr"), ("⌫", "back"), ("%", "op"), ("÷", "op")],
            [("7", "num"), ("8", "num"), ("9", "num"), ("×", "op")],
            [("4", "num"), ("5", "num"), ("6", "num"), ("−", "op")],
            [("1", "num"), ("2", "num"), ("3", "num"), ("+", "op")],
            [("±", "num"), ("0", "num"), (".", "num"), ("=", "eq")],
        ]

        for r, row in enumerate(layout):
            for c, (label, kind) in enumerate(row):
                self._make_btn(grid, label, kind, r, c)

    def _make_btn(self, parent, label, kind, row, col):
        if kind == "num":
            bg, fg, hov = BTN_NUM_BG, BTN_NUM_FG, HOVER_DARK
        elif kind == "op":
            bg, fg, hov = BTN_OP_BG, BTN_OP_FG, HOVER_OP
        elif kind == "eq":
            bg, fg, hov = BTN_EQ_BG, BTN_EQ_FG, HOVER_EQ
        else:
            bg, fg, hov = BTN_CLR_BG, BTN_CLR_FG, HOVER_CLR

        font = FONT_BTN_SM if label in ("⌫", "±") else FONT_BTN

        btn = tk.Button(
            parent,
            text=label,
            width=4,
            height=2,
            bg=bg,
            fg=fg,
            font=font,
            relief="flat",
            cursor="hand2",
            activebackground=hov,
            activeforeground="#ffffff",
            bd=0,
            highlightthickness=2,
            highlightbackground=fg,
            highlightcolor=hov,
            command=lambda l=label: self._on_press(l)
        )

        btn.grid(row=row, column=col, padx=6, pady=6, ipadx=3, ipady=3)

        btn.bind("<Enter>", lambda e, b=btn, h=hov: b.configure(bg=h, fg="#ffffff"))
        btn.bind("<Leave>", lambda e, b=btn, bg=bg, fg=fg: b.configure(bg=bg, fg=fg))

    def _on_press(self, label):
        if label == "C":
            self._expr = ""
            self._result = ""
            self._new_num = False
            self._update("0", "")

        elif label == "⌫":
            if self._new_num:
                self._expr = ""
                self._new_num = False
            self._expr = self._expr[:-1]
            self._update(self._expr or "0")

        elif label == "=":
            if not self._expr:
                return

            try:
                expr_py = (
                    self._expr
                    .replace("÷", "/")
                    .replace("×", "*")
                    .replace("−", "-")
                    .replace("%", "/100")
                )

                result = eval(expr_py)

                if isinstance(result, float) and result == int(result):
                    result = int(result)

                self._result = str(result)
                self._update(self._result, self._expr + " =")
                self._expr = self._result
                self._new_num = True

            except ZeroDivisionError:
                self._update("Error", "Cannot divide by zero")
                self._expr = ""

            except Exception:
                self._update("Error", "Invalid expression")
                self._expr = ""

        elif label == "±":
            if self._expr.startswith("-"):
                self._expr = self._expr[1:]
            else:
                self._expr = "-" + self._expr
            self._update(self._expr or "0")

        elif label == "%":
            self._expr += "%"
            self._update(self._expr)

        elif label in ("÷", "×", "−", "+"):
            if self._new_num:
                self._new_num = False
            self._expr += label
            self._update(self._expr)

        else:
            if self._new_num:
                self._expr = ""
                self._new_num = False
            self._expr += label
            self._update(self._expr)

    def _update(self, main_text, sub_text=None):
        self._main_var.set(main_text)
        if sub_text is not None:
            self._sub_var.set(sub_text)
        else:
            self._sub_var.set("")


if __name__ == "__main__":
    app = NeonCalculator()
    app.mainloop()