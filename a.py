import flet as ft

def main (pagina:ft.Page):
    pagina.bgcolor = "#363636"
    pagina.title = "Temperatura"
    pagina.window.height = 1000
    pagina.window.width = 900
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    pagina.vertical_alignment = ft.CrossAxisAlignment.CENTER

    def converter():
        a = float(valor.value)
        if x_temperatura.value == "Celsius" and y_temperatura.value == "Fahrenheit":
            resultado.value = round((a*1.8)+32,2)
        elif x_temperatura.value == "Celsius" and y_temperatura.value == "Kelvin":
            resultado.value = round(a + 273,2)
        elif x_temperatura.value == "Fahrenheit" and y_temperatura.value == "Celsius":
            resultado.value = round((a-32)/1.8,2)
        elif x_temperatura.value == "Fahrenheit" and y_temperatura.value == "Kelvin":
            resultado.value = round((a-32)*(1.8/9)+273,2)
        elif x_temperatura.value == "Kelvin" and y_temperatura.value == "Celsius":
            resultado.value = round(a - 273.15,2)
        elif x_temperatura.value == "Kelvin" and y_temperatura.value == "Fahrenheit":
            resultado.value = round(1.8*(a - 273.15) + 32,2)
        else:
            resultado.value = a

        if y_temperatura.value == "Celsius":
            tipo.value = "°C"
        elif y_temperatura.value == "Kelvin":
            tipo.value = "°K"
        else:
            tipo.value = "F"
       
    # Criando titulo

    titulo = ft.Text(value=  "TEMPERATURA",
                     size=40,
                     font_family="Arial",
                     color="#FFFFFF",
                     weight=ft.FontWeight.BOLD,)
                

    de = ft.Text(value=  "  DE   ",
                     size=14,
                     font_family="Arial",
                     color="#FFFFFF",
                     weight=ft.FontWeight.BOLD,
                    )

    para = ft.Text(value=  "PARA",
                     size=14,
                     font_family="Arial",
                     color="#FFFFFF",
                     weight=ft.FontWeight.BOLD,
                    )



    

    # Criando o Text box

    valor = ft.TextField(label="VALOR", 
                               hint_text="",
                               fill_color="#e2e2e2",
                               border_color="#2e3cfa",
                               width= 330
                               )

    x_temperatura =ft.Dropdown(
    filled= True,
    #border_radius= 
    color="#000000",
    border_color="#2e3cfa",
    fill_color="#e2e2e2",
    width=220,
    value="De",
    options=[
        ft.DropdownOption(key="Celsius", text="Celsius"),
        ft.DropdownOption(key="Fahrenheit", text="Fahrenheit"),
        ft.DropdownOption(key="Kelvin", text="Kelvin"),
    ],)
    
    y_temperatura = ft.Dropdown(

    filled= True,
    color="#000000",
    border_color="#2e3cfa",
    fill_color="#e2e2e2",
    width=220,
    value="Para",
    options=[
        ft.DropdownOption(key="Celsius", text="Celsius"),
        ft.DropdownOption(key="Fahrenheit", text="Fahrenheit"),
        ft.DropdownOption(key="Kelvin", text="Kelvin"),
    ],)


        
    textinho = ft.Text(value='Resultado:',
                       size=16,
                       font_family="Arial",
                        color="#FFFFFF",
                        weight=ft.FontWeight.BOLD,
                        )

    resultado = ft.Text(value='',
                        size=14,
                        font_family="Arial",
                        color="#FFFFFF",
                        weight=ft.FontWeight.BOLD,)

    tipo = ft.Text(value='',
                   color= "#ffffff",
                   weight=ft.FontWeight.BOLD,
                   )

        

    botao = ft.Button(content="Converter",
                      bgcolor = "#000000FF",
                      color= "#ffffff",
                      on_click=converter,
                      width= 120,
                      height=150,
                     )
                     
                      
                      

    

    # Adicionando itens

    coluna = ft.Column(controls=[de,
                                 x_temperatura,
                                 para,
                                 y_temperatura])
       
    linha = ft.Row(controls=[coluna,botao
                             ],
                             alignment= "center")

    
    
    pagina.controls=[titulo,
                     valor,
                     linha,
                     textinho,
                     resultado,
                     tipo,
                     ]

    pagina.update()

ft.run(main)