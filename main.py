import customtkinter as ctk
from backend import NU_CONSUME, consume_calc

#Interface
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        #UI congif
        self.geometry("800x800")
        self.iconbitmap("app_icon.ico")
        self.title("Calculadora de Fazendas")
        self.resizable(False,False)

        #main frame
        self.mainFrame = ctk.CTkFrame(self, fg_color="transparent")
        self.mainFrame.pack(fill="both", expand=True, padx=20, pady=20)
        self.uiCreate()

        self.labels_result = {}
        self.frameResults = ctk.CTkScrollableFrame(self.mainFrame, height=300, orientation="horizontal")
        self.frameResults.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        self.traducao_comidas = {
            "breadReq": "Pão",
            "stickReq": "Stick de Mascar",
            "coockedVegReq": "Vegetais Cozidos",
            "driedReq": "Carne Seca",
            "dustReq": "DustWich",
            "cubeReq": "Cubo de Comida",
            "gohanReq": "Gohan",
            "wrapReq": "Enrolado de Carne",
            "bowlReq": "Tigela de Arroz"
        }

        self.traducao_plantacoes = {
            "CA_S": "Cacto P",
            "CA_M": "Cacto M",
            "CA_L": "Cacto G",
            "CA_XL": "Cacto GG",
            "GF_S": "FrutV P",
            "GF_M": "FrutV M",
            "GF_L": "FrutV G",
            "GF_H": "FrutV H",
            "RW_S": "Arroz P",
            "RW_M": "Arroz M",
            "RW_L": "Arroz G",
            "RW_H": "Arroz H",
            "WS_S": "Trigo P",
            "WS_M": "Trigo M",
            "WS_L": "Trigo G",
            "WS_XL": "Trigo GG",
            "WS_H": "Trigo H"
        }
    
    def validate_integer(self, value):
        if value == "":
            return True
        return value.isdigit()


    def uiCreate(self):
        self.mainFrame.grid_columnconfigure((0, 1), weight=1)
        self.mainFrame.grid_rowconfigure((1, 2, 3), weight=1)

        #titulo
        self.frameTitulo = ctk.CTkFrame(self.mainFrame, fg_color="transparent")
        self.frameTitulo.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(0, 10)
            )
        
        self.lblTitle = ctk.CTkLabel(
            self.frameTitulo,
            text="Calculadora de Fazendas - KENSHI",
            font=("Arial", 22, "bold"),
            text_color="white"
            )
        self.lblTitle.pack()

        #seção 1
        self.frame1 = ctk.CTkFrame(self.mainFrame)
        self.frame1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.frame1.grid_columnconfigure(1, weight=1)

        self.titleFrame1 = ctk.CTkLabel(
            self.frame1,
            text="Nº por raça/tipo",
            font=("Arial", 17, "bold"),
            text_color="white"
        )
        self.lblGreen = ctk.CTkLabel(
            self.frame1,
            text="Camponês:",
            font=("Arial", 14, "bold"),
            text_color="white",
            padx=10,
        )
        self.lblScorch = ctk.CTkLabel(
            self.frame1,
            text="Beduíno:",
            font=("Arial", 14, "bold"),
            text_color="white",
            padx=10
        )
        self.lblShek = ctk.CTkLabel(
            self.frame1,
            text="Shek:",
            font=("Arial", 14, "bold"),
            text_color="white",
            padx=10
        )
        self.lblPrince = ctk.CTkLabel(
            self.frame1,
            text="Principe da Colônia:",
            font=("Arial", 14, "bold"),
            text_color="white",
            padx=10
        )
        self.lblDrone = ctk.CTkLabel(
            self.frame1,
            text="Operário da Colônia:",
            font=("Arial", 14, "bold"),
            text_color="white",
            padx=10
        )
        self.lblSoldier = ctk.CTkLabel(
            self.frame1,
            text="Soldado da Colônia:",
            font=("Arial", 14, "bold"),
            text_color="white",
            padx=10
        )
        self.lblDog = ctk.CTkLabel(
            self.frame1,
            text="Cachorro:",
            font=("Arial", 14, "bold"),
            text_color="white",
            padx=10
        )
        self.lblBeast = ctk.CTkLabel(
            self.frame1,
            text="Boi/Garru:",
            font=("Arial", 14, "bold"),
            text_color="white",
            padx=10
        )
        self.titleFrame1.grid(row=0, column=0, columnspan=2)
        self.lblGreen.grid(row=1, column=0, sticky="w")
        self.lblScorch.grid(row=2, column=0, sticky="w")
        self.lblShek.grid(row=3, column=0, sticky="w")
        self.lblPrince.grid(row=4, column=0, sticky="w")
        self.lblDrone.grid(row=5, column=0, sticky="w")
        self.lblSoldier.grid(row=6, column=0, sticky="w")
        self.lblDog.grid(row=7, column=0, sticky="w")
        self.lblBeast.grid(row=8, column=0, sticky="w")

        self.entryGreen = ctk.CTkEntry(
            self.frame1,
            width=100,
            height=10,
            text_color="white",
            placeholder_text="Ex: 10",
            validate="key",
            validatecommand=(self.register(self.validate_integer), "%P")
        )
        self.entryScorch = ctk.CTkEntry(
            self.frame1,
            width=100,
            height=10,
            text_color="white",
            placeholder_text="Ex: 10",
            validate="key",
            validatecommand=(self.register(self.validate_integer), "%P")
        )
        self.entryShek = ctk.CTkEntry(
            self.frame1,
            width=100,
            height=10,
            text_color="white",
            placeholder_text="Ex: 10",
            validate="key",
            validatecommand=(self.register(self.validate_integer), "%P")
        )
        self.entryPrince = ctk.CTkEntry(
            self.frame1,
            width=100,
            height=10,
            text_color="white",
            placeholder_text="Ex: 10",
            validate="key",
            validatecommand=(self.register(self.validate_integer), "%P")
        )
        self.entryDrone = ctk.CTkEntry(
            self.frame1,
            width=100,
            height=10,
            text_color="white",
            placeholder_text="Ex: 10",
            validate="key",
            validatecommand=(self.register(self.validate_integer), "%P")
        )
        self.entrySoldier = ctk.CTkEntry(
            self.frame1,
            width=100,
            height=10,
            text_color="white",
            placeholder_text="Ex: 10",
            validate="key",
            validatecommand=(self.register(self.validate_integer), "%P")
        )
        self.entryDog = ctk.CTkEntry(
            self.frame1,
            width=100,
            height=10,
            text_color="white",
            placeholder_text="Ex: 10",
            validate="key",
            validatecommand=(self.register(self.validate_integer), "%P")
        )
        self.entryBeast = ctk.CTkEntry(
            self.frame1,
            width=100,
            height=10,
            text_color="white",
            placeholder_text="Ex: 10",
            validate="key",
            validatecommand=(self.register(self.validate_integer), "%P")
        )
        self.entryGreen.grid(row=1, column=1, sticky="w")
        self.entryScorch.grid(row=2, column=1, sticky="w")
        self.entryShek.grid(row=3, column=1, sticky="w")
        self.entryPrince.grid(row=4, column=1, sticky="w")
        self.entryDrone.grid(row=5, column=1, sticky="w")
        self.entrySoldier.grid(row=6, column=1, sticky="w")
        self.entryDog.grid(row=7, column=1, sticky="w")
        self.entryBeast.grid(row=8, column=1, sticky="w")

        #seção 2
        self.frame2 = ctk.CTkFrame(self.mainFrame)
        self.frame2.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        self.frame2.grid_columnconfigure(1, weight=1)

        self.titleFrame2 = ctk.CTkLabel(
            self.frame2,
            text="Produtividade do solo",
            font=("Arial", 17, "bold"),
            text_color="white"
        )
        self.lblCactus = ctk.CTkLabel(
            self.frame2,
            text="Cactos:",
            font=("Arial", 14, "bold"),
            text_color="white",
            padx=10
        )
        self.lblGreenfruit = ctk.CTkLabel(
            self.frame2,
            text="Frutaverde:",
            font=("Arial", 14, "bold"),
            text_color="white",
            padx=10
        )
        self.lblRiceweed = ctk.CTkLabel(
            self.frame2,
            text="Ervarroz:",
            font=("Arial", 14, "bold"),
            text_color="white",
            padx=10
        )
        self.lblWheat = ctk.CTkLabel(
            self.frame2,
            text="Trigo:",
            font=("Arial", 14, "bold"),
            text_color="white",
            padx=10
        )
        self.titleFrame2.grid(row=0, column=0, columnspan=2)
        self.lblCactus.grid(row=1, column=0, sticky="w")
        self.lblGreenfruit.grid(row=2, column=0, sticky="w")
        self.lblRiceweed.grid(row=3, column=0, sticky="w")
        self.lblWheat.grid(row=4, column=0, sticky="w")

        self.entryCactus = ctk.CTkEntry(
            self.frame2,
            width=100,
            height=10,
            text_color="white",
            placeholder_text="Ex: 100, 97, 50",
            validate="key",
            validatecommand=(self.register(self.validate_integer), "%P")
        )
        self.entryGreenfruit = ctk.CTkEntry(
            self.frame2,
            width=100,
            height=10,
            text_color="white",
            placeholder_text="Ex: 100, 97, 50",
            validate="key",
            validatecommand=(self.register(self.validate_integer), "%P")
        )
        self.entryRiceweed = ctk.CTkEntry(
            self.frame2,
            width=100,
            height=10,
            text_color="white",
            placeholder_text="Ex: 100, 97, 50",
            validate="key",
            validatecommand=(self.register(self.validate_integer), "%P")
        )
        self.entryWheat = ctk.CTkEntry(
            self.frame2,
            width=100,
            height=10,
            text_color="white",
            placeholder_text="Ex: 100, 97, 50",
            validate="key",
            validatecommand=(self.register(self.validate_integer), "%P")
        )
        self.entryCactus.grid(row=1, column=1, sticky="w")
        self.entryGreenfruit.grid(row=2, column=1, sticky="w")
        self.entryRiceweed.grid(row=3, column=1, sticky="w")
        self.entryWheat.grid(row=4, column=1, sticky="w")

        #Botão para calcular
        self.calcButton = ctk.CTkButton(
            self.mainFrame,
            text_color="black",
            fg_color="#aaacad",
            hover_color="#c9c9c9",
            text="Calcular",
            command=self.calcular
        )
        self.calcButton.grid(row=2, column=0, columnspan=2)

    def calcular(self):
        green = float(self.entryGreen.get()) if self.entryGreen.get() else 0
        scorch = float(self.entryScorch.get()) if self.entryScorch.get() else 0
        shek = float(self.entryShek.get()) if self.entryShek.get() else 0
        prince = float(self.entryPrince.get()) if self.entryPrince.get() else 0
        drone = float(self.entryDrone.get()) if self.entryDrone.get() else 0
        soldier = float(self.entrySoldier.get()) if self.entrySoldier.get() else 0
        dog = float(self.entryDog.get()) if self.entryDog.get() else 0
        beast = float(self.entryBeast.get()) if self.entryBeast.get() else 0

        soilCactus = float(self.entryCactus.get()) if self.entryCactus.get() else 0
        soilFruit = float(self.entryGreenfruit.get()) if self.entryGreenfruit.get() else 0
        soilRice = float(self.entryRiceweed.get()) if self.entryRiceweed.get() else 0
        soilWheat = float(self.entryWheat.get()) if self.entryWheat.get() else 0

        for widget in self.frameResults.winfo_children():
            widget.destroy()

        food_req, prod_req = consume_calc(
            green,
            scorch,
            shek,
            prince,
            drone,
            soldier,
            dog,
            beast,
            soilCactus,
            soilFruit,
            soilRice,
            soilWheat
        )

        lbl_nome = ctk.CTkLabel(self.frameResults, text="Comida", font=("Arial", 14, "bold"))
        lbl_nome.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        lbl_qtd = ctk.CTkLabel(self.frameResults, text="Quantidade", font=("Arial", 14, "bold"))
        lbl_qtd.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        col = 2
        self.colFarms = []
        for key in self.traducao_plantacoes.keys():
            lbl = ctk.CTkLabel(
                self.frameResults,
                text=self.traducao_plantacoes[key], 
                font=("Arial", 14, "bold")
            )
            lbl.grid(row=0, column=col, padx=3, pady=5, sticky="w")
            self.colFarms.append(key)
            col += 1

        food_to_prod_map = {
            "breadReq": "breadProdReq",
            "stickReq": "chewProdReq",
            "coockedVegReq": "vegProdReq",
            "driedReq": "driedProdReq",
            "dustReq": "dustwProdReq",
            "cubeReq": "cubeProdReq",
            "gohanReq": "gohanProdReq",
            "wrapReq": "meatProdReq",
            "bowlReq": "bowlProdReq"
        }

        row = 1
        for food_key, food_name in self.traducao_comidas.items():
            if food_req.get(food_key, 0) == 0:
                continue

            ctk.CTkLabel(
                self.frameResults,
                text=food_name,
                font=("Arial", 14)
            ).grid(
                row=row,
                column=0,
                padx=5,
                pady=2,
                sticky="w"
            )

            ctk.CTkLabel(
                self.frameResults,
                text=str(food_req[food_key]),
                font=("Arial", 14)
            ).grid(
                row=row,
                column=1,
                padx=5,
                pady=2,
                sticky="w"
            )

            prod_key = food_to_prod_map.get(food_key)
            if prod_key and prod_key in prod_req:
                col = 2
                for plant_key in self.colFarms:
                    valor = prod_req[prod_key].get(plant_key, 0)
                    texto = str(valor) if valor > 0 else "-"
                    ctk.CTkLabel(
                        self.frameResults, 
                        text=texto, 
                        font=("Arial", 14)
                    ).grid(
                        row=row, 
                        column=col, 
                        padx=3, 
                        pady=2, 
                        sticky="w"
                    )
                    col += 1

            row += 1
        
app=App()
app.mainloop()