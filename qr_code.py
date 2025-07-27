import tkinter as tk
from tkinter import ttk, colorchooser, filedialog, messagebox
import numpy as np


class ScrollableFrame(tk.Frame):
    """Frame avec scrollbar verticale"""

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # Créer le canvas et la scrollbar
        self.canvas = tk.Canvas(self, bg='white', highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg='white')

        # Configurer le scrolling
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack les éléments
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Binding pour la molette de souris
        self.bind_mousewheel()

    def bind_mousewheel(self):
        """Lie la molette de souris au scrolling"""

        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        def _bind_to_mousewheel(event):
            self.canvas.bind_all("<MouseWheel>", _on_mousewheel)

        def _unbind_from_mousewheel(event):
            self.canvas.unbind_all("<MouseWheel>")

        self.canvas.bind('<Enter>', _bind_to_mousewheel)
        self.canvas.bind('<Leave>', _unbind_from_mousewheel)

class AdvancedQRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Générateur QR Code Avancé Pro")
        self.root.geometry("1200x800")  # Légèrement plus large
        self.root.configure(bg='#f0f0f0')

        # Style moderne
        self.setup_styles()

        # Variables
        self.text_var = tk.StringVar()
        self.qr_size = tk.IntVar(value=10)
        self.border_size = tk.IntVar(value=2)
        self.logo_size = tk.IntVar(value=20)
        self.fg_color = "#000000"
        self.bg_color = "#FFFFFF"
        self.gradient_color = "#0066cc"
        self.use_gradient = tk.BooleanVar(value=False)
        self.logo_path = None
        self.module_shape = tk.StringVar(value="square")
        self.error_correction = tk.StringVar(value="M")
        self.data_type = tk.StringVar(value="text")
        self.rotation_angle = tk.IntVar(value=0)
        self.add_shadow = tk.BooleanVar(value=False)
        self.pattern_style = tk.StringVar(value="standard")

        # Historique
        self.history = []

        # Interface utilisateur
        self.create_widgets()

        # QR Image
        self.qr_image = None

    def setup_styles(self):
        """Configure les styles modernes pour l'interface"""
        style = ttk.Style()
        style.theme_use('clam')

        # Couleurs modernes
        style.configure('Title.TLabel', font=('Helvetica', 16, 'bold'), foreground='#2c3e50')
        style.configure('Subtitle.TLabel', font=('Helvetica', 11, 'bold'), foreground='#34495e')
        style.configure('Modern.TButton', font=('Helvetica', 10, 'bold'))
        style.configure('Success.TButton', background='#27ae60', foreground='white')
        style.configure('Primary.TButton', background='#3498db', foreground='white')
        style.configure('Warning.TButton', background='#f39c12', foreground='white')

    def create_widgets(self):
        """Crée l'interface utilisateur moderne"""
        # En-tête
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=60)
        header_frame.pack(fill='x', pady=(0, 10))
        header_frame.pack_propagate(False)

        title_label = tk.Label(header_frame, text="🔲 Générateur QR Code Pro",
                               font=('Helvetica', 18, 'bold'),
                               fg='white', bg='#2c3e50')
        title_label.pack(pady=15)

        # Container principal avec deux colonnes
        main_container = tk.Frame(self.root, bg='#f0f0f0')
        main_container.pack(fill='both', expand=True, padx=10)

        # Colonne gauche - Contrôles avec scrollbar
        self.left_scrollable = ScrollableFrame(main_container)
        self.left_scrollable.pack(side='left', fill='both', expand=True, padx=(0, 5))

        # Colonne droite - Aperçu
        right_frame = tk.Frame(main_container, bg='white', relief='raised', bd=1)
        right_frame.pack(side='right', fill='both', expand=True, padx=(5, 0))

        # Utiliser le frame scrollable pour les contrôles
        left_frame = self.left_scrollable.scrollable_frame

        self.create_input_section(left_frame)
        self.create_style_section(left_frame)
        self.create_advanced_section(left_frame)
        self.create_actions_section(left_frame)
        self.create_preview_section(right_frame)

    def create_input_section(self, parent):
        """Section de saisie des données"""
        section = tk.LabelFrame(parent, text="📝 Contenu du QR Code",
                                font=('Helvetica', 11, 'bold'),
                                bg='white', fg='#2c3e50', padx=10, pady=5)
        section.pack(fill='x', padx=10, pady=5)

        # Type de données
        tk.Label(section, text="Type de contenu:", bg='white', font=('Helvetica', 10, 'bold')).pack(anchor='w',
                                                                                                    pady=(5, 0))
        type_frame = tk.Frame(section, bg='white')
        type_frame.pack(fill='x', pady=5)

        types = [("Texte", "text"), ("URL", "url"), ("Email", "email"),
                 ("Téléphone", "phone"), ("SMS", "sms"), ("WiFi", "wifi")]

        for i, (text, value) in enumerate(types):
            ttk.Radiobutton(type_frame, text=text, value=value,
                            variable=self.data_type,
                            command=self.on_type_change).grid(row=i // 3, column=i % 3, sticky='w', padx=5)

        # Zone de texte avec scrollbar
        tk.Label(section, text="Contenu:", bg='white', font=('Helvetica', 10, 'bold')).pack(anchor='w', pady=(10, 0))
        text_frame = tk.Frame(section, bg='white')
        text_frame.pack(fill='x', pady=5)

        self.text_entry = tk.Text(text_frame, height=4, wrap='word', font=('Helvetica', 10))
        scrollbar = ttk.Scrollbar(text_frame, orient='vertical', command=self.text_entry.yview)
        self.text_entry.configure(yscrollcommand=scrollbar.set)

        self.text_entry.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Boutons de templates rapides
        template_frame = tk.Frame(section, bg='white')
        template_frame.pack(fill='x', pady=5)
        tk.Label(template_frame, text="Templates rapides:", bg='white', font=('Helvetica', 9)).pack(anchor='w')

        templates = [("Site Web", "https://"), ("Email", "mailto:"), ("Téléphone", "tel:")]
        for text, template in templates:
            ttk.Button(template_frame, text=text,
                       command=lambda t=template: self.insert_template(t)).pack(side='left', padx=2)
