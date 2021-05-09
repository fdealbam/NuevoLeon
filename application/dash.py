#NUEVO LEON 

import os
import pandas as pd

#Abre bd
entidades_s= pd.read_csv("https://raw.githubusercontent.com/fdealbam/censo2020/main/entidades2020.csv")#, encoding= "Latin-1")
entidades_p= pd.read_csv("https://raw.githubusercontent.com/fdealbam/censo2020/main/entidades2020percent.csv")#, encoding="Latin-1")

#pormunicipio_fa.replace(to_replace ="*",
#                 value =0, inplace=True)


# Falta un identificador de la base 1) entidad 2)mpios
df = entidades_s[entidades_s.ENTIDAD == 19]
df_p = entidades_p[entidades_p.ENTIDAD == 19]


noment = df.iloc[0]["NOM_ENT"]

#-------------------------------------Pob Total
ptotal_s                                             = df.POBTOT.sum()      # población total  
pfemto_s                                             = df.POBFEM.sum()      # población femenina 
pmascu_s                                             = df.POBMAS.sum()      # población masculina 

#-------------------------------------Derechohabiencia
sinderechohabiencia_s                                = df.PSINDER.sum()      # Población sin afiliación a servicios de salud  
derechoimss_s                                        = df.PDER_IMSS.sum()    # Población afiliada a servicios de salud en el IMSS  
derechosegp_s                                        = df.PDER_SEGP.sum()    # Población afiliada a servicios de salud en el Instituto de Salud para el Bienestar
derechopriv_s                                        = df.PAFIL_IPRIV.sum()  # Población afiliada a servicios de salud en una institución privada 


#-------------------------------------Educación (Primaria completa cambió por analfabetismo)
poblacion15ymasanalfabeta_s                          = df.P15YM_AN.sum()    # Población de 15 años y más analfabeta             
poblacion15ymasconsecundaria_s                       = df.P15SEC_CO.sum()   # Población de 15 años y más con secundaria completa
poblacion15ymasconposbasica_s                        = df.P18YM_PB.sum()    # Población de 18 años y más con educación posbásica




#-------------------------------------Discapacidad|
condiscapacidad_s                                    = df.PCON_DISC.sum()    # Población con discapacidad
 
#Edad 
de60añosymas_s                                       = df.P_60YMAS.sum()     # población de 60 y más          
de15a64años_s                                        = df.POB15_64.sum()     # población de 15 a 64 años         
de15A17años_s                                        = df.P_15A17.sum()      # población de 15 a 17 años         
de12a14años_s                                        = df.P_12A14.sum()      # población de 12 a 14 años         
de6a11años_s                                         = df.P_6A11.sum()       # población de 6 a 11 años       
de3a5años_s                                          = df.P_3A5.sum()        # población de 3 a 5 años      
de0a2años_s                                          = df.P_0A2.sum()        # población de 0 a 2 años      

#Vivienda
#-------------------------------------             Variables de Vivienda
consanitario_s                                       = df.VPH_EXCSA.sum()    # Viviendas particulares habitadas que disponen de excusado o sanitario     
vivendashabitadas_s                                  = df.VIVTOT.sum()       # Total de viviendas        
conluzelectrica_s                                    = df.VPH_C_ELEC.sum()   # Viviendas particulares habitadas que disponen de energía eléctrica             
conaguaentubada_s                                    = df.VPH_AGUADV.sum()   # Viviendas particulares habitadas que disponen de agua entubada en el ámbito de la viviendas           
conundorm_s                                          = df.VPH_1DOR.sum()     # Viviendas particulares habitadas con un dormitorio                        
condrenaje_s                                         = df.VPH_DRENAJ.sum()   # Viviendas particulares habitadas que disponen de drenaje            
contelevisor_s                                       = df.VPH_TV.sum()       # Viviendas particulares habitadas que disponen de televisor                  
conrefrigerador_s                                    = df.VPH_REFRI.sum()    # Viviendas particulares habitadas que disponen de refrigerador                
constreaming_s                                       = df.VPH_SPMVPI.sum()   # Viviendas particulares habitadas que disponen de servicio de películas, música o videos de paga por Internet           
coninternet_s                                        = df.VPH_INTER.sum()    # Viviendas particulares habitadas que disponen de Internet                         
concomputadora_s                                     = df.VPH_PC.sum()       # Viviendas particulares habitadas que disponen de computadora, laptop o tablet       
concelular_s                                         = df.VPH_CEL.sum()      # Viviendas particulares habitadas que disponen de teléfono celular
continaco_s                                          = df.VPH_TINACO.sum()   # Viviendas particulares habitadas que disponen de tinaco 
concisterna                                          = df.VPH_CISTER.sum()   # Viviendas particulares habitadas que disponen de cisterna o aljibe
conlavadora_s                                        = df.VPH_LAVAD.sum()    # Viviendas particulares habitadas que disponen de lavadora    
conbici_s                                            = df.VPH_BICI.sum()     # Viviendas particulares habitadas que disponen de bicicleta como medio de transporte 


#----------------------------------------------------Variables de Migración
poblacionnacidaenotraentidad_s                       = df.PNACOE.sum()       # Población nacida en otra entidad                 
poblacionfemeninanacidaenotraentidad_s               = df.PNACOE_F.sum()     # Población femenina nacida en la entidad               
poblacionde15añosymasnacidaotraentidad_s             = df.PRESOE15.sum()     # Población de 5 años y más residente en otra entidad en marzo de 2015      


#----------------------------------------------------Variables de economía
poblacionOcupada_s                                   = df.POCUPADA.sum()     # población ocupada          
poblacionMasculinaOcupada_s                          = df.POCUPADA_M.sum()   # Población femenina de 12 años y más desocupada           
poblacionFemeninaOcupada_s                           = df.POCUPADA_F.sum()   # Población masculina de 12 años y más ocupada                                           
poblacion12ymasdesocupada_s                          = df.PDESOCUP.sum()     # Población de 12 años y más desocupada  
poblacioninactiva_s                                  = df.PE_INAC.sum()                       


#----------------------------------------------------Variables de Religión 
religioncatolica_s                                   = df.PCATOLICA.sum()    # Población con religión católica           
sinreligion_s                                        = df.PSIN_RELIG.sum()   # Población sin religión o sin adscripción religiosa  
evangelistasyprotestante_s                           = df.PRO_CRIEVA.sum()   # Población con grupo religioso protestante/ cristiano evangélico              
otrasreligioness_s                                   = df.POTRAS_REL.sum()   # Población con otras religiones diferentes a las anteriores  

#----------------------------------------------------Variables de Educación
poblacion15ymasanalfabeta_s                          = df.P15YM_AN.sum()     # Población de 15 años y más analfabeta          

#----------------------------------------------------Variables de Hogares censales
             
poblacionenhogaresconjefaturafemenina_s              = df.HOGJEF_F.sum()     # Hogares censales con persona de referencia mujer             
poblacionenhogaresconjefaturamasculina_s             = df.PHOGJEF_M.sum()    # Hogares censales con persona de referencia hombre
poblaciontotalenhogares_s                            = df.POBHOG.sum()       # Población en hogares censales
#agregados:jef masc y total de hogares

promediodeocupantesporvivienda                      =  df.PROM_OCUP.sum()    #Promedio de ocupantes en viviendas particulares habitadas





############################################################################### PORCEnTAJES



# PORCEnTAJES
#---------------------------------Pob Total
#ptotal_p                                             = df_p['POBTOT_%'].sum()
pfemto_p                                             = (df_p['POBFEM_%'].sum()).round(1)
pmascu_p                                             = df_p['POBMAS_%'].sum()

#---------------------------------Derechohabiencia
sinderechohabiencia_p                                = df_p['PSINDER_%'].sum()
derechoimss_p                                        = df_p['PDER_IMSS_%'].sum()
derechosegp_p                                        = df_p['PDER_SEGP_%'].sum()
derechopriv_p                                        = df_p['PAFIL_IPRIV_%'].sum()


#---------------------------------Educación (Primaria completa cambió por analfabetismo)
#poblacion15ymasanalfabeta_p                           = df_p['P15YM_AN_%'].sum()

#---------------------------------Discapacidad
condiscapacidad_p                                    = df_p['PCON_DISC_%'].sum()
 
#Edad 
de60añosymas_p                                       = df_p['P_60YMAS_%'].sum()              
de15a64años_p                                        = df_p['POB15_64_%'].sum()              
de15A17años_p                                        = df_p['P_15A17_%'].sum()              
de12a14años_p                                        = df_p['P_12A14_%'].sum()              
de6a11años_p                                         = df_p['P_6A11_%'].sum()              
de3a5años_p                                          = df_p['P_3A5_%'].sum()              
de0a2años_p                                          = df_p['P_0A2_%'].sum()              

#Vivienda
#---------------------------------Variables de Vivienda
consanitario_p                                       = df_p['VPH_EXCSA_%'].sum()        
vivendashabitadas_p                                  = df_p['TVIVHAB_%'].sum()              
conluzelectrica_p                                    = df_p['VPH_C_ELEC_%'].sum()              
conaguaentubada_p                                    = df_p['VPH_AGUADV_%'].sum()              
conundorm_p                                          = df_p['VPH_1DOR_%'].sum()                            
condrenaje_p                                         = df_p['VPH_DRENAJ_%'].sum()              
contelevisor_p                                       = df_p['VPH_TV_%'].sum()                        
conrefrigerador_p                                    = df_p['VPH_REFRI_%'].sum()                   
constreaming_p                                       = df_p['VPH_SPMVPI_%'].sum()              
coninternet_p                                        = df_p['VPH_INTER_%'].sum()                            
concomputadora_p                                     = df_p['VPH_PC_%'].sum()              
concelular_p                                         = df_p['VPH_CEL_%'].sum()  
continaco_p                                          = df_p['VPH_TINACO_%'].sum() 
concisterna                                          = df_p['VPH_CISTER_%'].sum()
conlavadora_p                                        = df_p['VPH_LAVAD_%'].sum()  
conbici_p                                            = df_p['VPH_BICI_%'].sum()


#---------------------------------Variables de Migración
poblacionnacidaenotraentidad_p                       = df_p['PNACOE_%'].sum()                
poblacionfemeninanacidaenotraentidad_p               = df_p['PNACOE_F_%'].sum()               
poblacionde15añosymasnacidaotraentidad_p             = df_p['PRESOE15_%'].sum()       


#---------------------------------Variables de economía
poblacionOcupada_p                                   = (df_p['POCUPADA_%'].sum()).round(1)              
poblacionMasculinaOcupada_p                          = (df_p['POCUPADA_M_%'].sum()).round(1)              
poblacionFemeninaOcupada_p                           = (df_p['POCUPADA_F_%'].sum()).round(1)                                             
poblacioninactiva_p                                  = (df_p['PE_INAC_%'].sum()).round(1)                       
poblacion12ymasdesocupada_p                          = (df_p['PDESOCUP_%'].sum()).round(1)     


#---------------------------------Variables de Religión 
religioncatolica_p                                   = df_p['PCATOLICA_%'].sum()              
sinreligion_p                                        = df_p['PSIN_RELIG_%'].sum()    
evangelistasyprotestante_p                           = df_p['PRO_CRIEVA_%'].sum()              
otrasreligioness_p                                   = df_p['POTRAS_REL_%'].sum()  

#---------------------------------Variables de Educación
poblacion15ymasanalfabeta_p                          = df_p['P15YM_AN_%'].sum()              
poblacion15ymasconsecundaria_p                       = df_p['P15SEC_CO_%'].sum()
poblacion15ymasconposbasica_p                        = df_p['P18YM_PB_%'].sum()

#---------------------------------Variables de Hogares censales
             
poblacionenhogaresconjefaturafemenina_p              = (df_p['PHOGJEF_F_%'].sum()).round(1)               
poblacionenhogaresconjefaturamasculina_p             = (df_p['PHOGJEF_M_%'].sum()).round(1)
poblaciontotalenhogares_p                            =  df_p['POBHOG_%'].sum()





import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
import dash_table
import sidetable as stb
import datetime
from datetime import datetime, timedelta
from datetime import date
#import geopandas as gpd
import flask
import os
yesterday = datetime.now() - timedelta(1)
yea = datetime.strftime(yesterday, '%Y%m%d')

today = date.today()
d2 = today.strftime("Fecha de actualización : %d-%m-%Y")

#pobsindh = 7804407




##########################################################################
#Seccion 1. Variables de POBLACION
##########################################################################



################################## Card

card = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Variables", 
                    className="card-title",
                    style={'textAlign': 'left',"color": "gray"}),
            html.H2("de población", 
                    className="card-subtitle",
                    style={'textAlign': 'left',"color": "black", "font-weight": 'bold'}),
            html.Br(),
            html.Br(),
            html.Br(),
          
            html.P(
                "Sin derechohabiencia "
               f"{int(sinderechohabiencia_s):,}",
                className="card-text",
                style={'textAlign': 'left',"color": "black",
                   #'FontColor': 120
                      }
            ),

            
            
            dbc.Button(
                html.Span(["", html.H1(className="fas fa-male", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-male", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-male", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-male", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-male", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-male", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-male", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-male", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-male", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-male", style={"color": "#E0E0E0"}),]),),
            html.Br(),
            
            
            
            #Porcentaje derechohabiencia 
          
            html.P([(sinderechohabiencia_p),"%"] ,   
                  className="card-text",
                  style={'textAlign': 'right',
                         "color": "black",  
                         "font-size": "48px",
                         "font-weight": 'bold',
                        "color": "dark",}),
         
            dbc.Button(
                html.Span([html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),

                          ],style={"align" :"center",
                                   'margin-left': '-30px',
                                   #'margin-right': '120px',
                                  }),),
          
            
            
            
            
            # 15 años y más analfabeta
            html.P(
                "Población de 15 años y más analfabeta "   #verificar este campo (alfabeta* o analfabeta)
               f"{int(poblacion15ymasanalfabeta_s):,}",    
                className="card-text",
                style={'textAlign': 'left',"color": "black",
                   'FontColor': 120}
            ),
            dbc.Button(
                html.Span(["", html.H1(className="fas fa-user-graduate", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#E0E0E0"}),
                          ]),),
            
            # % 15 años y más analfabeta
             html.P([(poblacion15ymasanalfabeta_p),"%"] ,
                  className="card-text",
                  style={'textAlign': 'right',
                         "color": "black",  
                         "font-size": "48px",
                         "font-weight": 'bold',}),
            

            dbc.Button(
                html.Span([html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),

                          ],style={"align" :"center",
                                   'margin-left': '-30px',
                                  }),),
            
             html.P(
                "Con discapacidad " 
                f"{int(condiscapacidad_s):,}",   
                className="card-text",
                style={'textAlign': 'left',"color": "black",
                   'FontColor': 120}
            ),
            dbc.Button(
                html.Span(["", html.H1(className="fas fa-wheelchair", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#E0E0E0"}),]),),
            html.P([(condiscapacidad_p),"%"] , 
                  className="card-text",
                    style={'textAlign': 'right',
                         "color": "black",  
                         "font-size": "48px",
                         "font-weight": 'bold',}),

        ]
    ),
    
    style={"width": "22.5rem", 
          "border": "0",
           "card-border": "0"},
)





##########################################################################
#Seccion 2. Variables de vivienda
##########################################################################

#################################### Card2 HAY QUE AJUSTARLA CON....


card2 = dbc.Card(
    dbc.CardBody(
        [   
             #Falta Poblacion total
            html.H6("Población total", 
                    style={#'textAlign': 'left',
                           "color": "white",
                          "background-color": "orange"}),
            html.H3(f"{int(ptotal_s):,}",
                    style={#'textAlign': 'left',
                           "color": "white",
                          "background-color": "orange"}),
            dbc.Button(
                html.Span([html.H1(className="fas fa-male", style={"color":   "white"}),
                           html.H1(className="fas fa-female", style={"color": "white"}),
                           html.H1(className="fas fa-male", style={"color":   "white"}),
                           html.H1(className="fas fa-female", style={"color": "white"}),
                           html.H1(className="fas fa-female", style={"color": "white"}),
                           html.H1(className="fas fa-male", style={"color":   "white"}),
                           html.H1(className="fas fa-female", style={"color": "white"}),
                           html.H1(className="fas fa-male", style={"color":   "white"}),
                           html.H1(className="fas fa-female", style={"color": "white"}),
                           html.H1(className="fas fa-male", style={"color":   "white"}),
                           html.H1(className="fas fa-female", style={"color": "white"}),
                           html.H1(className="fas fa-male", style={"color":   "white"}),
                           html.H1(className="fas fa-female", style={"color": "white"}),
                           html.H1(className="fas fa-male", style={"color":   "white"}),
                           html.H1(className="fas fa-female", style={"color": "white"}),
                           html.H1(className="fas fa-male", style={"color":   "white"}),
                           html.H1(className="fas fa-female", style={"color": "white"}),
                          ],style={#"background-color": "orange"
                                  }),style={"background-color": "orange"}),

            
              #Falta Poblacion masculina y femenina
#             html.Span([
#                html.H6([pfemto_p, "%  "], style={"color": "white", "background-color": "orange"}), 
#                html.H1(className="fas fa-female",  
#                                  style={"color": "white", "background-color": "orange"}),
#
#                html.H6([pmascu_p, "%  "], style={"color": "white", "background-color": "orange"}), 
#                html.H1(className="fas fa-male",  
#                                  style={"color": "white", "background-color": "orange"}),
# 
#        ]),
                           
        ]), 
                            style={"width": "25rem", 
                                   "border": "0",
                                   "margin-left": "-10px",
                                   #"height": "10px",
                                   "background-color": "orange",
                                  },) 

            

card21 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("De 0 a 2 años ", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5( f"{int(de0a2años_s):,}", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
           
          
            html.P([(de0a2años_p),"%"] , #"64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                            "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]), 
                            style={"width": "25.5rem", 
                                   "border": "0",
                                   #"height": "10px",
                                   "background-color": "#0097A7",
                                  },)

card22 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("De 3 a 5 años", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5(f"{int(de3a5años_s ):,}",
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
             html.P([(de3a5años_p),"%"] , 
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]), 
                            style={"width": "25.5rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
   
   },),
  
card23 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("De 6 a 11 años", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5(f"{int(de6a11años_s):,}",
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            
            html.P([(de6a11años_p),"%"] , 
           
                  style={'textAlign': 'right',
                         "color": "white",
                            "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]), 
                            style={"width": "25.5rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                  },),

card24 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("De 12 a 14 años", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5(f"{int(de12a14años_s):,}", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            
            html.P([(de12a14años_p),"%"] ,
         
                  style={'textAlign': 'right',
                         "color": "white",
                            "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',
                         })]), 
                            style={"width": "25.5rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                  },)
                               
 
   

card25 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("De 15 a 17 años", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5(f"{int(de15A17años_s):,}",
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            
             html.P([(de15A17años_p),"%"] ,
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',
                        })]), 
                            style={"width": "25.5rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                  },)

card26 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("De 15 a 64 años", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5(f"{int(de15a64años_s):,}",
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            
             html.P([(de15a64años_p),"%"] ,
            
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]), 
                            style={"width": "25.5rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                  },)

card27 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("De 60 años y más", #Aqui cambio antes: "De 18 años y más"
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5(f"{int(de60añosymas_s):,}",  
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            
            html.P([(de60añosymas_p),"%"] ,
             
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]), 
                            style={"width": "25.5rem", 
                                      "border": "0",
                                      "background-color": "#0097A7",
                                  },)


##########################################################################
#Seccion 3. Variables de vivienda
##########################################################################
   
               



## Tabla de variablesvar
row1 = html.Tr([
                html.Td([dbc.Button([html.H6(className="fas fa-home",
                                style={'textAlign': 'left',
                                       "color":"#FBC02D",
                                      "font-size": "40px",
                                       "margin-right": "-120px",
                                       "margin-top": "-20px",
                                      "widht": "10px"})])]),    
                dbc.Alert("Con sanitario", color="#E0E0E0",
                        style={"text-align": "right",
                               "margin-left": "-120px",
                              "height": "50px" }),
                html.Td(f"{int(consanitario_s):,}",
                         style={"height": "50px",
                               "text-align": "top"}),
   
                dbc.Alert( [(consanitario_p),"%"] ,#"94%", 
                          color="light",
                        style={"font-size": "35px",
                               "height": "40px",
                              "margin-left": "-40px",
                               
                        "font-weight": 'bold',
                        "color": "#FBC02D",       
                        })])


row2 = html.Tr([
                html.Td([dbc.Button([html.H6(className="fas fa-home",
                                style={'textAlign': 'left',
                                       "color":"#FBC02D",
                                      "font-size": "40px",
                                       "margin-right": "-120px",
                                       "margin-top": "-20px",
                                      "widht": "10px"})])]),    
                dbc.Alert("Viviendas habitadas", color="#E0E0E0",
                        style={"text-align": "right",
                               "margin-left": "-120px",
                              "height": "50px" }),
                html.Td(f"{int(vivendashabitadas_s):,}", 
                         style={"height": "50px",
                               "text-align": "top"}),
    
                dbc.Alert([(vivendashabitadas_p),"%"],#"94%",
                          color="light",
                        style={"font-size": "35px",
                               "height": "40px",
                              "margin-left": "-40px",
                               "font-weight": 'bold',
                               "color": "#FBC02D",
                              })])
     


row3 = html.Tr([
                html.Td([dbc.Button([html.H6(className="fas fa-home",
                                style={'textAlign': 'left',
                                       "color":"#FBC02D",
                                      "font-size": "40px",
                                       "margin-right": "-120px",
                                       "margin-top": "-20px",
                                      "widht": "10px"})])]),    
                dbc.Alert("Con luz eléctrica", color="#E0E0E0",
                        style={"text-align": "right",
                               "margin-left": "-120px",
                              "height": "50px" }),
                html.Td(f"{int(conluzelectrica_s):,}", 
                         style={"height": "50px",
                               "text-align": "top"}),
    
                dbc.Alert([(conluzelectrica_p),"%"],#"94%",
                          color="light",
                        style={"font-size": "35px",
                               "height": "40px",
                              "margin-left": "-40px",
                               "font-weight": 'bold',
                               "color": "#FBC02D",
                              })])


row4 = html.Tr([
                html.Td([dbc.Button([html.H6(className="fas fa-home",
                                style={'textAlign': 'left',
                                       "color":"#FBC02D",
                                      "font-size": "40px",
                                       "margin-right": "-120px",
                                       "margin-top": "-20px",
                                      "widht": "10px"})])]),    
                dbc.Alert("Con agua entubada", color="#E0E0E0",
                        style={"text-align": "right",
                               "margin-left": "-120px",
                              "height": "50px" }),
                html.Td(f"{int(conaguaentubada_s):,}", 
                         style={"height": "50px",
                               "text-align": "top"}),
                dbc.Alert([(conaguaentubada_p),"%"],#"94%",
                          color="light",
                        style={"font-size": "35px",
                               "height": "40px",
                              "margin-left": "-40px",
                               
                        "font-weight": 'bold',
                        "color": "#FBC02D",       
                        })])


row5 = html.Tr([
                html.Td([dbc.Button([html.H6(className="fas fa-home",
                                style={'textAlign': 'left',
                                       "color":"#FBC02D",
                                      "font-size": "40px",
                                       "margin-right": "-120px",
                                       "margin-top": "-20px",
                                      "widht": "10px"})])]),    
                dbc.Alert("Con drenaje", color="#E0E0E0",
                        style={"text-align": "right",
                               "margin-left": "-120px",
                              "height": "50px" }),
                html.Td(f"{int(condrenaje_s):,}",
                         style={"height": "50px",
                               "text-align": "top"}),
                dbc.Alert([(condrenaje_p),"%"],#"94%",
                          color="light",
                        style={"font-size": "35px",
                               "height": "40px",
                              "margin-left": "-40px",
                               
                        "font-weight": 'bold',
                        "color": "#FBC02D",       
                        })])


table_body = [html.Tbody([row2, row1, row3, row4,row5])]




#################################### Card3
card3 = dbc.Card(
    dbc.CardBody(
        [
            
            html.P([dbc.Button([html.H1(className="fas fa-home",
                                style={'textAlign': 'left',
                                       "color":"#FBC02D",
                                      "font-size": "80px"}),
            "  Variables de Vivienda"], 
                    style={'textAlign': 'left',"color":"#FBC02D",
                   "font-size": "30px",
                           'margin-bottom':'-30px'
                          })]),
            
     dbc.Table( table_body, bordered=False)]),
    
    
    style={"width": "50rem", 
          "border": "0",
          "fill" : "orange"},
)



##########################################################################
#Seccion 4 Variables de INTERNET
##########################################################################
      
#Falta por acomodar nuevas variables:       
#f"{int(conundorm_s):,}",              
#                      
#f"{int(conrefrigerador_s):,}",        
#f"{int(constreaming_s):,}",                       
#f"{int(continaco_s):,}",              
#f"{int(concisterna):,}",              
#f"{int(conlavadora_s):,}",            
#f"{int(conbici_s):,}", 
#################################### Card2p3
card2p3 = dbc.Card(
    dbc.CardBody(
        [
         dbc.Button((["", html.H3(className="fas fa-wifi", style={"color": "black",
                                                                 "background-color": "light"}),
                 html.H6(" Con internet ",
                        style={"color":"black",
                               "font-size":10,
                                "background-color": "light"}),
                 html.H4([(coninternet_p),"%"],#"97%",
                        style={"color":"#FBC02D",
                                "background-color": "light"}),
                 html.P(f"{int(coninternet_s):,}", style={"font-size":10}),                      
        ]),style={ "background-color": "light"}),

            
         dbc.Button((["", html.H3(className="fas fa-tv", 
                                  style={"color": "lightgray",
                                         "background-color": "light"}),
                 html.H6(" Con televisor ", 
                         style={"color":"lightgray",
                                 "font-size":10,
                                "background-color": "light"}),
                 html.H4([(contelevisor_p),"%"],#"97%",  
                         style={"color":"#FBC02D",
                                "background-color": "light"}),
                 html.P(f"{int(contelevisor_s):,}",  style={"font-size":10}),                      
        ]),style={ "background-color": "light"}),

         dbc.Button((["", html.H3(className="fas fa-laptop", style={"color": "lightgray",
                                                                   "background-color": "light"}),
                 html.H6(" Con computadora ",
                         style={"color":"lightgray",
                                 "font-size":10,
                                "background-color": "light"}),
                 html.H4([(concomputadora_p),"%"],#"97%",
                        style={"color":"#FBC02D",
                                "background-color": "light"}),# 
                 html.P(f"{int(concomputadora_s):,}", style={"font-size":10}),                      
        ]),style={ "background-color": "light"}),
            

         dbc.Button((["", html.H3(className="fas fa-mobile-alt", style={"color": "black",
                                                                       "background-color": "light"}),
                 html.H6(" Con celular ",
                        style={"color":"black",
                                "font-size":10,
                                "background-color": "light"}),
                 html.H4([(concelular_p),"%"],#"97%",
                        style={"color":"#FBC02D",
                                "background-color": "light"}),
                 html.P(f"{int(concelular_s):,}", style={"font-size":10}),                      
        ]),style={ "background-color": "light"}),
        
#poner aqui refrigerador            
         dbc.Button((["", html.H3(className="fas fa-mobile-alt", style={"color": "black",
                                                                       "background-color": "light"}),
                 html.H6(" Con refrigerador ",
                        style={"color":"black",
                                "font-size":10,
                                "background-color": "light"}),
                 html.H4([(conrefrigerador_p),"%"],#"97%",
                        style={"color":"#FBC02D",
                                "background-color": "light"}),
                 html.P(f"{int(conrefrigerador_s):,}", style={"font-size":10}),                      
        ]),style={ "background-color": "light"}),
            

#poner aqui lavadora            
         dbc.Button((["", html.H3(className="fas fa-washer", style={"color": "black",
                                                                       "background-color": "light"}),
                 html.H6(" Con lavadora ",
                        style={"color":"black",
                                "font-size":10,
                                "background-color": "light"}),
                 html.H4([(conlavadora_p),"%"],#"97%",
                        style={"color":"#FBC02D",
                                "background-color": "light"}),
                 html.P(f"{int(conlavadora_s):,}", style={"font-size":10}),                      
        ]),style={ "background-color": "light"}),


#poner aqui bicicleta            
         dbc.Button((["", html.H2(className="fas fa-bicycle", style={"color": "black",
                                                                       "background-color": "light"}),
                 html.H6(" Con bicicleta",
                        style={"color":"black",
                                "font-size":10,
                                "background-color": "light"}),
                 html.H4([(conbici_p),"%"],#"97%",
                        style={"color":"#FBC02D",
                                "background-color": "light"}),
                 html.P(f"{int(conbici_s):,}", style={"font-size":10}),                      
        ]),style={ "background-color": "light"}),
            
     
        ]), style={"width": "45rem",
                   "margin-left": "46.5px",
                   "margin-right": "46.5px",
                   "border": "0",
                   "background-color": "light",
                  "outline": "white"
                #  "border-width": "1px"
                  })


        




##########################################################################
#Seccion 7. Variables de MIGRACION
##########################################################################
             
      

card_migra1 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Población nacida en otra entidad", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#9cd9e0"}),
            html.H5(f"{int(poblacionnacidaenotraentidad_s):,}", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#9cd9e0"}),
            html.H2([(poblacionnacidaenotraentidad_p),"%"],#"64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]), 
                            style={"width": "48rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#9cd9e0",
                                  },)

card_migra2 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Población femenina nacida en otra entidad", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5(f"{int(poblacionfemeninanacidaenotraentidad_s):,}",
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            html.H2([(poblacionfemeninanacidaenotraentidad_p),"%"],#"64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]), 
                            style={"width": "48rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                  },)

card_migra3 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Población de 5 años y más residente en otra entidad en marzo de 2015", # cambio: Población de 5 años y mas nacida en otra entidad otranota: VERIFICAR "en marzo de 2015"
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5(f"{int(poblacionde15añosymasnacidaotraentidad_s):,}",    
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            html.H2([(poblacionde15añosymasnacidaotraentidad_p),"%"],#"64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]), 
                            style={"width": "48rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                  },)


#################################### card_v_migracion
#"fas fa-hospital-user"
#"fas fa-procedures"
card_v_migracion = dbc.Card(
    dbc.CardBody([
        html.P([dbc.Button([html.H1(className="fas fa-plane-departure",
                                style={'textAlign': 'left',
                                       "color":"#0097A7",
                                      "font-size": "80px"}),
            "  Variables de migración"], 
                    style={'textAlign': 'left',"color":"#0097A7",
                   "font-size": "30px",
                          })]),
        
        dbc.Card(card_migra1),
        html.Br(),
        dbc.Card(card_migra2),
        html.Br(),
        dbc.Card(card_migra3),
        
    ],  style={"width": "50rem", 
           "border": "0",
           "fill" : "orange"},))


    
##########################################################################
#Seccion 8. Variables de HOGARES CENSALES
##########################################################################

row1 = html.Tr([dbc.Alert("Población en hogares" , color="E0E0E0",), 
                html.Td(f"{int(poblaciontotalenhogares_s):,}"),
                dbc.Alert([(poblaciontotalenhogares_p),"%"], color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#F48FB1",       
                        })])


row2 = html.Tr([dbc.Alert("Población en hogares con jefatura masculina", color="#E0E0E0",), 
                html.Td(f"{int(poblacionenhogaresconjefaturamasculina_s):,}"),
                dbc.Alert([(poblacionenhogaresconjefaturamasculina_p),"%"], color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#F48FB1",       
                        })])

row3 = html.Tr([dbc.Alert("Población en hogares con jefatura femenina", color="#E0E0E0",), 
                html.Td(f"{int(poblacionenhogaresconjefaturafemenina_s):,}"),
                dbc.Alert([(poblacionenhogaresconjefaturafemenina_p),"%"],
                          color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#F48FB1",       
                        })])

row4 = html.Tr([dbc.Alert("Promedio de ocupantes en viviendas particulares", color="#E0E0E0",), 
                html.Td("    "),
                dbc.Alert(promediodeocupantesporvivienda, color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#F48FB1",       
                        })])

table_body = [html.Tbody([row1, row2, row3, row4])]



#################################### card_v_hog_cens

           
card_v_hog_cens = dbc.Card(
    dbc.CardBody(
        [

        html.P([dbc.Button([html.H1(className= "fas fa-users",
                                    #"fas fa-house",
                                style={'textAlign': 'left',
                                       "color":"#F48FB1",
                                      "font-size": "80px"}),
            "  Variables de hogares censales"], 
                    style={'textAlign': 'left',"color":"#F48FB1",
                   "font-size": "30px",
                           'margin-bottom':'-30px'
                          })]),            
            
            
     dbc.Table( table_body, bordered=False)
                    ]),
    
    
    style={"width": "50rem", 
          "border": "0",
          "fill" : "orange"},
)

    
##########################################################################
#Seccion 9. Variables de DISCAPACIDAD
##########################################################################

row1 = html.Tr([dbc.Alert("Población con discapacidad", color="#E0E0E0",), 
                html.Td(f"{int(condiscapacidad_s):,}"),
                dbc.Alert([(condiscapacidad_p),"%"],# "4%",
                          color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#BA68C8",       
                        })])

#Ya no está
#row2 = html.Tr([dbc.Alert("Poblacion con discapacidad derechohabiente", color="#E0E0E0",), 
#                html.Td("19,172,575"),
#                dbc.Alert("59%", color="light",
#                        style={"font-size": "35px",
#                        "font-weight": 'bold',
#                        "color": "#BA68C8",       
#                        })])
#
table_body = [html.Tbody([row1, #row2,
                         ])]


card_v_discapacidad = dbc.Card(
    dbc.CardBody(
        [
            
            html.P([dbc.Button([html.H1(className="fa fa-wheelchair",
                                style={'textAlign': 'left',
                                       "color":"#BA68C8",
                                      "font-size": "80px"}),
            "  Variables de Discapacidad"], 
                    style={'textAlign': 'left',"color":"#BA68C8",
                   "font-size": "30px",
                           'margin-bottom':'-30px'
                          })]),
            
     dbc.Table( table_body, bordered=False)
                    ]),
                    style={"width": "50rem", 
                          "border": "0",
                          "fill" : "orange"},
        )


##########################################################################
#Seccion 10. Variables de ECONOMIA
##########################################################################


card_econom1 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Población ocupada", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#9cd9e0"}),
            html.H5(f"{int(poblacionOcupada_s):,}", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#9cd9e0"}),
            html.H2([(poblacionOcupada_p),"%"],# "95%", 
                  style={'textAlign': 'right',
                         "color": "white",
                            "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]),style={"width": "36rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#9cd9e0",
                                    },)




card_econom2 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Población masculina ocupada", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5(f"{int(poblacionMasculinaOcupada_s):,}", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            html.H2([(poblacionMasculinaOcupada_p),"%"],#"95%", 
                  style={'textAlign': 'right',
                         "color": "white",
                            "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]),style={"width": "36rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                    },)


card_econom3 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Población femenina ocupada", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#9cd9e0"}),
            html.H5(f"{int(poblacionFemeninaOcupada_s):,}", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#9cd9e0"}),
            html.H2([(poblacionFemeninaOcupada_p),"%"],# "95%", 
                  style={'textAlign': 'right',
                         "color": "white",
                            "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]),style={"width": "36rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#9cd9e0",
                                    },)


card_econom4 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("12 años y más, no activa y estudiante", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5(f"{int(poblacioninactiva_s):,}", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            html.H2([(poblacioninactiva_p),"%"],#"95%", 
                  style={'textAlign': 'right',
                         "color": "white",
                            "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]),style={"width": "36rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                    },)

card_economia = dbc.Card(
    dbc.CardBody(
        [
            html.P([dbc.Button([html.H1(className="fas fa-hand-holding-usd",
                                style={'textAlign': 'left',
                                       "color":"#0097A7",
                                      "font-size": "80px"}),
            "  Variables de economía"], 
                    style={'textAlign': 'left',"color":"#0097A7",
                   "font-size": "30px",
                          })],),
            dbc.Card(card_econom1),
            html.Br(),
            dbc.Card(card_econom2),
            html.Br(),
            dbc.Card(card_econom3),
            html.Br(),
            dbc.Card(card_econom4),
        ],style={"width": "38rem", }))
            

    
    
    
    
    
    
card_economia_discap = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Población de 12 años y más desocupada", 
                    style={'textAlign': 'left',
                           "color": "white",
                           "background-color": "#6A1B9A"}),
            html.H3(f"{int(poblacion12ymasdesocupada_s):,}", 
                    style={'textAlign': 'left',
                                      "color": "white",
                                      "background-color": "#6A1B9A"}),
            html.Br(),
            html.Br(),
            
            dbc.ButtonGroup(html.Span([
                html.H1(className="fas fa-user-minus", 
                        style={"background-color": "#6A1B9A",
                               "color":"white",
                               "font-size": "110px",
                              #'size':'80px',
                              'textAlign': 'center',
                               #'margin-left':'10px'
                              }),]),),
            html.Br(),
            html.Br(),
            
            html.H2([(poblacion12ymasdesocupada_p),"%"], 
                  style={'textAlign': 'center',
                         "color": "white",
                            #"height": "7px",
                         "font-size": "40px",
                         #'margin-top': '-32px',
                         #'margin-bottom': '30px',
                         "background-color": "#6A1B9A"}),]),
    style={"width": "13rem", 
          "border": "0",
           #"margin-left": "40px",
          "background-color": "#6A1B9A",
           'color':'#BA68C8',
           "height": "550px",
          })


##########################################################################
#Seccion 5 Variables de RELIGION
##########################################################################
card_religion1 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Religión católica", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#9cd9e0"}),
            html.H5(f"{int(religioncatolica_s):,}",   
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#9cd9e0"}),
            html.H2([(religioncatolica_p),"%"],#"64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]), 
                            style={"width": "48rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#9cd9e0",
                                  },)

card_religion2 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Protestantes, Evangélicas y diferentes de Evangélicas", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5(f"{int(evangelistasyprotestante_s):,}",
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            html.H2([(evangelistasyprotestante_p),"%"],#"64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]), 
                            style={"width": "48rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                  },)


card_religion3 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Sin religión", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#9cd9e0"}),
            html.H5(f"{int(sinreligion_s):,}",       
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#9cd9e0"}),
            html.H2([(sinreligion_p),"%"],#"64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]), 
                            style={"width": "48rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#9cd9e0",
                                  },)
card_religion4 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Otras religiones", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5(f"{int(otrasreligioness_s):,}",     
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            html.H2([(otrasreligioness_p),"%"],#"64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]), 
                            style={"width": "48rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                  },)

#########
card_v_religionAA = dbc.Card(
    dbc.CardBody(
        [
            html.P([dbc.Button([html.H1(className="fas fa-church",
                                style={'textAlign': 'left',
                                       "color":"#0097A7",
                                      "font-size": "80px"}),
            "  Variables de Religion"], 
                    style={'textAlign': 'left',"color":"#0097A7",
                   "font-size": "30px",
                          })]),
            
            dbc.Card(card_religion1),
            html.Br(),
            dbc.Card(card_religion2),
            html.Br(),
            dbc.Card(card_religion3),
            html.Br(),
            dbc.Card(card_religion4),
            
        ]),
    style={"width": "50rem", 
           "border": "0",
           "fill" : "orange"},
)










##########################################################################
#Seccion 6 Variables de EDUCACION
##########################################################################


row1edu = html.Tr([dbc.Alert("De 15 años y más analfabeta", color="#E0E0E0",), 
                html.Td(f"{int(poblacion15ymasanalfabeta_s):,}"),
                dbc.Alert([(poblacion15ymasanalfabeta_p),"%"], color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#81C784",       
                        })])


row2edu = html.Tr([dbc.Alert("De 15 años y más con secundaria completa", color="#E0E0E0",), 
                html.Td(f"{int(poblacion15ymasconsecundaria_s):,}"),
                dbc.Alert([(poblacion15ymasconsecundaria_p),"%"], color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#81C784",       
                        })])

row3edu = html.Tr([dbc.Alert("De 18 años y más con educación posbásica", color="#E0E0E0",), 
                html.Td(f"{int(poblacion15ymasconposbasica_s):,}"),
                dbc.Alert([(poblacion15ymasconposbasica_p),"%"],color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#81C784",       
                        })])

table_body = [html.Tbody([row1edu, row2edu, row3edu])]



#################################### card_v_edu

           
card_v_edu = dbc.Card(
    dbc.CardBody(
        [
         html.P([dbc.Button([html.H1(className="fas fa-book-reader",
                                style={'textAlign': 'left',
                                       "color":"#81C784",
                                      "font-size": "80px"}),
            "  Variables de educación"], 
                    style={'textAlign': 'left',"color":"#81C784",
                   "font-size": "30px",
                           'margin-bottom':'-30px'
                          })]),
            
     dbc.Table( table_body, bordered=False)
                    ]),
    
    
    style={"width": "50rem", 
     #   "border":"none",
     #    "border-color": "transparent",
    #"background-color": "transparent",
     #     " border-bottom":" 1px solid rgba(0,0,0,.8)",
          # "border": "0",
          # "border-top":"0",
          # "border-right":"0",
          # "border-bottom":"0",
          # "border-left":"0",
          #  "padding": "0",
          # "card-border": 0,
           "border-color": "white",
           
         },
)
    

    

##########################################################################
#Seccion 7. Variables de DERECHOHABIENCIA
##########################################################################


card_derechohab1 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Derechohabiente del IMSS", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#9cd9e0"}),
            html.H5(f"{int(derechoimss_s):,}",
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#9cd9e0"}),
            html.H2([(derechoimss_p),"%"],#"%"
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]), 
                            style={"width": "48rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#9cd9e0",
                                  },)

card_derechohab2 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Derechohabiente del Instituto de Salud para el Bienestar", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5(f"{int(derechosegp_s):,}", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            html.H2([(derechosegp_p),"%"],#"64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]), 
                            style={"width": "48rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                  },)
                
#################################### card_v_derechohab
#"fas fa-hospital-user"
#"fas fa-procedures"
card_v_derechohab = dbc.Card(
    dbc.CardBody([
        html.P([dbc.Button([html.H1(className="fas fa-procedures",
                                style={'textAlign': 'left',
                                       "color":"#0097A7",
                                      "font-size": "80px"}),
            "  Variables de derechohabiencia"], 
                    style={'textAlign': 'left',"color":"#0097A7",
                   "font-size": "30px",
                          })]),
        
        dbc.Card(card_derechohab1),
        html.Br(),
        dbc.Card(card_derechohab2),]),
    style={"width": "50rem", 
           "border": "0",
           "fill" : "orange"},)
    
    
    
    
    
########################################################################
# A P P 
########################################################################



# identificadores

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
server = flask.Flask(__name__)    
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. 
                                                LUX, FONT_AWESOME], server=server)


# make a reuseable navitem for the different examples
nav_item1 = dbc.NavItem(dbc.NavLink("Inicio", href="https://plataformacenso2020.herokuapp.com/"))
nav_item2 = dbc.NavItem(dbc.NavLink("Entidades", href="#"))
nav_item3 = dbc.NavItem(dbc.NavLink("Metrópolis", href="#"))



default = dbc.NavbarSimple(
    children=[nav_item1,nav_item2,nav_item3],
    brand="MENU",  style={"font-size": "12px"},
    brand_href="#",
    sticky="top",
    className="mb-12",
)

body = html.Div([
    dbc.Row(
           [
               dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/CamaraDiputados/blob/main/application/static/logocamara.jfif?raw=true",
                        ),width ={ "size": 1,  "offset": 1,
                                  "height": "5px"}),
               dbc.Col(html.H4("Reporte estadístico básico de ",
                        style={'offset' : 0, "size": 6,
                              "margin-left": "-122px",
                               "font-size": "12px",
                              "color": "grey",
                               "height": "5px",
                              'textAlign': 'center',
                               #"font-weight": 'bold',
                               "font-family": "Montserrat"
                              })),
                      ], justify= "center"),               
    dbc.Row(
           [
               dbc.Col(html.H1(noment,
                        style={ "size": 6, "offset":2,
                              "font-size": "35px",
                               "height": "40px",
                              "color": "dark",
                              'textAlign': 'center',
                               #"font-weight": 'bold',
                               "font-family": "Montserrat",
                              },)),
                      ], justify= "center"),            
    
    #Cintillo 00    
    dbc.Row(
           [
               dbc.Col(html.H6(d2),           #Fecha de actualización
               width={'size' : "auto",
                      'offset' : 1,
                      #'textAlign': 'center',
                     }), 
            ], justify= "center"),
    dbc.Row(
           [
               dbc.Col(html.H6("Fuente: Censo 2020, INEGI"),
                        width={'size' : "auto",
                               #"offset":1,
                              'textAlign': 'center',
                               "color": "grey",
}),
            ], justify= "center"),
               
    html.Br(),
    

    
    ################## SECCION 1 (pag1)_VARIABLES DE POBLACION
    dbc.Row([
        dbc.Col(dbc.Card(card), sm={  "offset": 1, }),#Variables Vivienda
        dbc.Col(dbc.Card(card2),                      #población total
               style={#'margin-top': '-540px',       #arriba
                      'margin-left': '40px', 
               #       'width': '479px',
               #       'height': '100%',
               }, sm={  "offset": 1, })
     ], className="blockquote"),
    
    dbc.Row([
        dbc.Col(dbc.Card(card21), #cuadros azules
                style={'margin-top': '-678px', #arriba
                       'margin-left': '467px', 
                       'width': '382px',
                       'height': '379px',})
    ]),
    
    dbc.Row([
       dbc.Col(dbc.Card(card22),#cuadros azules
               style={'margin-top': '-593px', #arriba
                      'margin-left': '467px', 
                      'width': '382px',
                      'height': '379px',
                     })
    ]),

    dbc.Row([
        dbc.Col(dbc.Card(card23),#cuadros azules
                style={'margin-top': '-508px', #arriba
                       'margin-left': '467px', 
                       'width': '382px',
                       'height': '379px',})
    ]),

     dbc.Row([
       dbc.Col(dbc.Card(card24),#cuadros azules
               style={'margin-top': '-423px', #arriba
                      'margin-left': '467px', 
                      'width': '382px',
                      'height': '379px',
                     })
    ]),
      dbc.Row([
       dbc.Col(dbc.Card(card25),#cuadros azules
               style={'margin-top': '-338px', #arriba
                      'margin-left': '467px', 
                      'width': '382px',
                      'height': '379px',
                     })
    ]),
       dbc.Row([
      dbc.Col(dbc.Card(card26, outline=False),#cuadros azules
              style={'margin-top': '-293px', #arriba
                     'margin-left': '467px', 
                     'width': '382px',
                      'height': '279px',
                   })
    ]),
         dbc.Row([
       dbc.Col(dbc.Card(card27),#cuadros azules
               style={'margin-top': '-208px', #arriba
                      'margin-left': '467px', 
                      'width': '382px',
                      'height': '19px',
                     })
    ]),
    
    ################## SECCION 2 (pag1)_VARIABLES DE VIVIENDA
    dbc.Row([
       
  
        
        dbc.Col(dbc.Card(card3, color="white", inverse=True, outline =False  ),sm={  "offset": 1, }),
         
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),


    
    ################## SECCION 4 (pag1)_VARIABLES DE INTERNET

    dbc.Row([
        dbc.Col(dbc.Card(card2p3, color="green"),
         sm={  "offset": 1, }),
    
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),
    html.Br(),
    

    
    ################## SECCION 5 (pag1)__VARIABLES DE MIGRACION
     
    dbc.Row([
        dbc.Col(dbc.Card(card_v_migracion), #cuadros azules
                sm={ 'size': 9.5,
                    "offset": 1, }),
                 ], style={"border": "0px",
                          "border-color": "red",
                          "border-width": "0px"}, 
                    no_gutters= True, justify= "start",
                 className="blockquote"),

    
    
    #############################>>>>>>> II <<<<<<<<<#############################
    
    ################## SECCION 1 (pag 2)__VARIABLES DE DISCAPACIDAD
    dbc.Row([
        dbc.Col(dbc.Card(card_v_discapacidad, #color="#FBFBFB", outline=True,
                         #inverse=False
                        ),
         sm={"offset": 1, }),
         
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),

    
 
    
    dbc.Row([
        dbc.Col(dbc.Card(card_economia), sm={  "offset": 1, }),#Variables Vivienda
        dbc.Col(dbc.Card(card_economia_discap),                      #población total
               style={#'margin-top': '-540px',       #arriba
                      'margin-left': '15px',
                   "color":"#BA68C8"
               #       'width': '479px',
               #       'height': '100%',
               }, sm={  "offset": 1, })
     ],  no_gutters= True, justify= "start",
     className="blockquote"),
    
 

    # ejemplo card in card
    dbc.Row([
        dbc.Col(dbc.Card(card_v_religionAA),
                sm={  "offset": 1, }),
    ], no_gutters= True, justify= "start",
     className="blockquote",
     ),
    
    
    #############################>>>>>>> III <<<<<<<<<#############################
    
    ################## SECCION 1 (3a pag)__VARIABLES DE EDUCACION      
    dbc.Row([
        dbc.Col(dbc.Card(card_v_edu, #color="#FBFBFB", outline=True,
                         #inverse=False
                        ),
         sm={  "offset": 1, }),
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),
    
    
    ################## SECCION 2 (3a pag)__VARIABLES DE DERECHOHABIENCIA
    dbc.Row([
        dbc.Col(dbc.Card(card_v_derechohab, #color="#FBFBFB", outline=True,
                         #inverse=False
                        ),
         sm={ "offset": 1, }),
     ], no_gutters= True, justify= "start",
     className="blockquote",),
    
    ################## SECCION 3 (3a pag)__VARIABLES DE HOGARES CENSALES 
    dbc.Row([
        dbc.Col(dbc.Card(card_v_hog_cens, #color="#FBFBFB", outline=True,
                         #inverse=False
                        ),
         sm={  "offset": 1, }),
     ], no_gutters= True, justify= "start",
     className="blockquote",),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    
    dbc.Row([
                                    #https://github.com/fdealbam/CamaraDiputados/blob/b11ef31e8e0f73e1a4a06ce60402563e1bd0122e/application/static/logocamara.jfif
           dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/CamaraDiputados/blob/main/application/static/logocamara.jfif?raw=true"),
                        width=5, md={'size': 1,  "offset": 3, }),
            
           dbc.Col(html.H6(" S e c r e t a r í a   G e n e r a l," 
                           " Secretaría de Servicios Parlamentarios, "
                           " México, 2021 "),
                  width={'size': 5, 'offset': 0}),
               ], justify="start",),
     dbc.Row([    
           dbc.Col(html.H5([dbc.Badge("Equipo responsable", 
                          href="https://innovation-learning.herokuapp.com/",
                                     )]),
                  width={'size': 3,  "offset": 4}),
                       ], justify="start",),
    html.Br(),
    html.Br(),
    html.Br(),

    

    
    html.Br(),
        
            ])
    

app.layout = html.Div(
    [default, body])
#app.layout = html.Div(children=[html.Img(className='icon')])

if __name__ == '__main__':
    app.run_server(use_reloader = False)
