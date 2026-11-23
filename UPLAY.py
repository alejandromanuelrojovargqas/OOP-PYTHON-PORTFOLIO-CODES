import tkinter as tk
from tkinter import messagebox


class LoginWindow:
    """Vista de inicio de sesión con estética oscura y acentos rosa-morados."""

    # Paleta de colores (dark + neon pink/purple)
    BG_MAIN = "#0B0A10"
    BG_CARD = "#151221"
    BG_INPUT = "#1F1A30"
    BORDER_CARD = "#3B1D6E"

    TEXT_BRIGHT = "#FFFFFF"
    TEXT_SOFT = "#E2D9F3"
    TEXT_NEON_PINK = "#FF5CE1"
    TEXT_NEON_PURPLE = "#C77DFF"

    BTN_PRIMARY = "#9D4EDD"
    BTN_PRIMARY_HOVER = "#F72585"
    BTN_SECONDARY_BG = "#151221"
    BTN_SECONDARY_FG = "#FF5CE1"

    def __init__(self, root: tk.Tk, on_login_success=None):
        self._root = root
        self._on_login_success = on_login_success

        self._root.title("sign in to UPLAY")
        self._root.geometry("420x520")
        self._root.minsize(380, 480)
        self._root.configure(bg=self.BG_MAIN)

        # Variables de control para los campos
        self._email_var = tk.StringVar()
        self._password_var = tk.StringVar()
        self._status_var = tk.StringVar(value="")

        self._build_ui()

    def _build_ui(self) -> None:
        """Construye los contenedores y widgets del login."""
        outer_frame = tk.Frame(self._root, bg=self.BG_MAIN, padx=24, pady=24)
        outer_frame.pack(fill=tk.BOTH, expand=True)

        # Tarjeta central
        card = tk.Frame(
            outer_frame,
            bg=self.BG_CARD,
            highlightbackground=self.BORDER_CARD,
            highlightthickness=2,
            padx=28,
            pady=28,
        )
        card.pack(fill=tk.BOTH, expand=True)

        # Encabezado
        lbl_badge = tk.Label(
            card,
            text="✦ PLAY AND BE HAPPY ✦",
            font=("Segoe UI", 9, "bold"),
            fg=self.TEXT_NEON_PINK,
            bg=self.BG_CARD,
        )
        lbl_badge.pack(anchor="w")

        lbl_title = tk.Label(
            card,
            text="Welcome Back",
            font=("Segoe UI", 24, "bold"),
            fg=self.TEXT_BRIGHT,
            bg=self.BG_CARD,
        )
        lbl_title.pack(anchor="w", pady=(4, 2))

        lbl_subtitle = tk.Label(
            card,
            text="Log in to find people & events you vibe with",
            font=("Segoe UI", 10),
            fg=self.TEXT_SOFT,
            bg=self.BG_CARD,
        )
        lbl_subtitle.pack(anchor="w", pady=(0, 22))

        # Campo: Email o Username
        lbl_email = tk.Label(
            card,
            text="Email or Username",
            font=("Segoe UI", 10, "bold"),
            fg=self.TEXT_NEON_PURPLE,
            bg=self.BG_CARD,
        )
        lbl_email.pack(anchor="w", pady=(0, 6))

        self._entry_email = self._create_styled_entry(card, self._email_var)
        self._entry_email.pack(fill=tk.X, pady=(0, 16))
        self._entry_email.focus_set()

        # Campo: Password
        lbl_password = tk.Label(
            card,
            text="Password",
            font=("Segoe UI", 10, "bold"),
            fg=self.TEXT_NEON_PURPLE,
            bg=self.BG_CARD,
        )
        lbl_password.pack(anchor="w", pady=(0, 6))

        self._entry_password = self._create_styled_entry(
            card, self._password_var, show="*"
        )
        self._entry_password.pack(fill=tk.X, pady=(0, 8))

        # Mensaje de validación / estado
        lbl_status = tk.Label(
            card,
            textvariable=self._status_var,
            font=("Segoe UI", 9, "bold"),
            fg=self.TEXT_NEON_PINK,
            bg=self.BG_CARD,
            wraplength=310,
            justify="left",
        )
        lbl_status.pack(anchor="w", pady=(0, 14))

        # Botón principal rosa-morado
        btn_login = tk.Button(
            card,
            text="LOG IN",
            font=("Segoe UI", 11, "bold"),
            fg=self.TEXT_BRIGHT,
            bg=self.BTN_PRIMARY,
            activebackground=self.BTN_PRIMARY_HOVER,
            activeforeground=self.TEXT_BRIGHT,
            relief=tk.FLAT,
            bd=0,
            cursor="hand2",
            pady=11,
            command=self._handle_login,
        )
        btn_login.pack(fill=tk.X, pady=(0, 12))
        self._bind_hover(btn_login, self.BTN_PRIMARY_HOVER, self.BTN_PRIMARY)

        # Botón secundario para crear cuenta (placeholder por ahora)
        btn_register = tk.Button(
            card,
            text="Create an account",
            font=("Segoe UI", 10, "bold"),
            fg=self.BTN_SECONDARY_FG,
            bg=self.BTN_SECONDARY_BG,
            activebackground=self.BG_INPUT,
            activeforeground=self.TEXT_BRIGHT,
            relief=tk.FLAT,
            bd=0,
            cursor="hand2",
            pady=8,
            command=self._handle_register_placeholder,
        )
        btn_register.pack(fill=tk.X)

        # Permitir presionar Enter para iniciar sesión
        self._root.bind("<Return>", lambda _event: self._handle_login())

    def _create_styled_entry(
        self, parent: tk.Widget, var: tk.StringVar, show: str = ""
    ) -> tk.Entry:
        """Crea un campo de texto oscuro con borde brillante al enfocar."""
        entry = tk.Entry(
            parent,
            textvariable=var,
            show=show,
            font=("Segoe UI", 11),
            fg=self.TEXT_BRIGHT,
            bg=self.BG_INPUT,
            insertbackground=self.TEXT_NEON_PINK,
            relief=tk.FLAT,
            highlightthickness=2,
            highlightbackground=self.BORDER_CARD,
            highlightcolor=self.TEXT_NEON_PINK,
        )
        entry.config(
            insertwidth=2,
        )
        # Padding interno simulado vía contenedor para mayor compatibilidad
        wrapper = tk.Frame(
            parent,
            bg=self.BG_INPUT,
            highlightthickness=2,
            highlightbackground=self.BORDER_CARD,
            highlightcolor=self.TEXT_NEON_PINK,
        )
        entry_inner = tk.Entry(
            wrapper,
            textvariable=var,
            show=show,
            font=("Segoe UI", 11),
            fg=self.TEXT_BRIGHT,
            bg=self.BG_INPUT,
            insertbackground=self.TEXT_NEON_PINK,
            relief=tk.FLAT,
            bd=0,
        )
        entry_inner.pack(fill=tk.X, padx=10, pady=9)

        # Cambia el borde del wrapper cuando el entry gana o pierde foco
        entry_inner.bind(
            "<FocusIn>",
            lambda _e: wrapper.config(highlightbackground=self.TEXT_NEON_PINK),
        )
        entry_inner.bind(
            "<FocusOut>",
            lambda _e: wrapper.config(highlightbackground=self.BORDER_CARD),
        )
        # Guardamos referencia para focus_set()
        self._last_inner_entry = entry_inner
        return wrapper

    @staticmethod
    def _bind_hover(widget: tk.Widget, hover_bg: str, normal_bg: str) -> None:
        """Agrega efecto hover al pasar el mouse."""
        widget.bind("<Enter>", lambda _e: widget.config(bg=hover_bg))
        widget.bind("<Leave>", lambda _e: widget.config(bg=normal_bg))

    def _handle_login(self) -> None:
        """Valida entradas básicas (calidad) antes de autenticar."""
        identifier = self._email_var.get().strip()
        password = self._password_var.get()

        if not identifier or not password:
            self._status_var.set("Please fill in both fields.")
            return

        if len(password) < 4:
            self._status_var.set("Password must be at least 4 characters.")
            return

        self._status_var.set("")
        if self._on_login_success:
            self._on_login_success(identifier)
        else:
            messagebox.showinfo(
                "Login Ready",
                f"Session check passed for: {identifier}\n(Ready to connect with User & DB)",
            )

    def _handle_register_placeholder(self) -> None:
        """Espacio reservado para el flujo de registro."""
        self._status_var.set("Registration view coming next.")


if __name__ == "__main__":
    main_root = tk.Tk()
    app = LoginWindow(main_root)
    # Pequeño ajuste para que el foco inicial caiga dentro del input real
    if hasattr(app, "_last_inner_entry"):
        app._last_inner_entry.focus_set()
    main_root.mainloop()