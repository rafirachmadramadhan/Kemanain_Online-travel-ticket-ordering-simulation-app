from kivy.config import Config
Config.set('graphics', 'multisamples', '0')
#Config.set('graphics', 'width', '540')
#Config.set('graphics', 'height', '980')
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.properties import StringProperty, BooleanProperty, NumericProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.core.audio import SoundLoader,Sound
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.factory import Factory
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.snackbar import Snackbar
from kivy.utils import get_color_from_hex
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivy.uix.image import AsyncImage,Image
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.label import MDLabel
from kivy.metrics import dp, sp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineIconListItem
from kivy.core.window import Window
#Window.release_all_keyboards()
from kivymd.uix.button import MDFlatButton
from kivy.utils import platform
from datetime import datetime, timedelta
from kivymd.uix.fitimage.fitimage import FitImage
import random
#Window.softinput_mode = "below_target"
#Window.softinput_mode = "resize"
Window.softinput_mode = "pan"
#h = datetime.now()
#h1 = h+timedelta(1)
#h2 = +timedelta(2)
#print((datetime.now()+timedelta()).strftime("%d %B %Y"))

if platform != "android":
    Window.size = (350*1.2, 650*1.2)

ep=[["Lion Air",1301100, "4.00", "5.30", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Surabaya", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air",1515300, "5.00", "6.30", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Surabaya", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air",3448900, "6.00", "7.30", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Surabaya", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 5509500, "6.30", " 8.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Surabaya", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 5509500, "8.00", "9.30", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Surabaya", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia",6426500, "10.30", "12.00", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Surabaya", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia",1828300, "13.00", "14.30", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Surabaya", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 1515300, "18.00", "19.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],  
    ["Citilink", 5509500, "19.00", "20.40", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],  
    ["Citilink", 5500000, "16.40", "19.40", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Citilink", 7509500, "19.00", "20.40", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta()).strftime("%d %B %Y"),"First"],  
    ["Citilink", 7500000, "16.40", "19.40", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta()).strftime("%d %B %Y"),"First"],  
    ["Batik Air", 2424500, "9.00", "11.05", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya","Bali", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 9552500, "11.00", "13.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya","Bali", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Air Asia", 641200, "15.30", "17.25", "https://awards.brandingforum.org/wp-content/uploads/2016/05/airasia-feat-logo.jpg","Surabaya","Bali", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Air Asia", 650000, "17.00", "19.00", "https://awards.brandingforum.org/wp-content/uploads/2016/05/airasia-feat-logo.jpg","Surabaya","Bali", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Sriwijaya Air", 2708000, "17.30", "19.20", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Surabaya","Bali", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Nam Air", 1424960, "18.50", "21.40", "http://inaca.or.id/wp-content/uploads/2018/07/logo-NAM-air.png","Jakarta","Bali", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Air Asia", 1486900, "16.25", "19.15", "https://awards.brandingforum.org/wp-content/uploads/2016/05/airasia-feat-logo.jpg","Jakarta","Bali", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Sriwijaya Air", 2708000, "17.30", "19.20", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Jakarta","Bali", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 4220600, "6.30", " 9.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Bali", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 6602600, "4.30", " 7.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Bali", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 6761900, "9.10", "12.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Banjarmasim", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 6761900, "15.00", "17.50", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Banjarmasim", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 5907000, "13.00", "15.50", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Banjarmasim", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 10151400, "5.00", "12.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Banjarmasim", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 14363400, "7.00", "15.50", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Surabaya","Banjarmasim", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 1875400, "14.10", "18.30", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Pontianak", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 1875400, "19.00", "23.10", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Pontianak", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 5774200, "19.00", "23.10", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Pontianak", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 11444100, "18.40", "23.00", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Surabaya","Pontianak", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Lion Air", 862200, "17.00", "18.30", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Pontianak", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air", 862200, "19.00", "20.30", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Pontianak", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Super Air Jet", 889400, "17.00", "18.30", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Pontianak", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Super Air Jet", 889200, "20.00", "21.30", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Pontianak", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 3818800, "15.30", "17.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Pontianak", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 3818800, "16.00", "17.30", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Pontianak", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Super Air Jet", 1290300, "4.45", "8.10", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Sriwijaya Air", 1398320, "13.35", "17.00", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Jakarta","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 1972655, "14.00", "17.25", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],  
    ["Sriwijaya Air", 2060990, "22.00", "1.25", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Jakarta","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Garuda Indonesia", 2366100, "22.05", "1.30", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Garuda Indonesia", 4530600, "1.30", "5.05", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 7261200, "15.10", "18.45", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"First"],
    ["Garuda Indonesia", 4530600, "22.05", "1.25", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 3340100, "5.30", "8.55", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Pontianak", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 3340100, "9.40", "13.05", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Pontianak", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Citilink", 1307681, "6.00", "8.25", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Surabaya","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],  
    ["Citilink", 1430681, "6.00", "8.25", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Surabaya","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],  
    ["Lion Air", 1272100, "16.20", "18.50", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Surabaya","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Sriwijaya Air", 1486900, "19.20", "21.50", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Surabaya","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Sriwijaya Air", 1486900, "19.50", "22.20", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Surabaya","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 2427900, "5.00", "7.30", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 6729700, "5.00", "7.30", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"First"],
    ["Batik Air", 7510600, "7.00", "13.05", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Denpasar", "Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 13105900, "19.25", "1.25", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Denpasar","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"First"],
    ["Garuda Indonesia", 13105900, "18.40", "1.25", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Denpasar","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"First"],
    ["Garuda Indonesia", 13105900, "19.25", "7.40", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Denpasar","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"First"],
    ["Lion Air", 1906400, "8.35", "12.50", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Denpasar","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air", 1226400, "12.10", "13.30", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Denpasar","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 1312337, "15.30", "17.00", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Denpasar","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],  
    ["Sriwijaya Air", 1019720, "19.25", "20.45", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Denpasar","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Nam Air", 2010190, "17.45", "19.00", "http://inaca.or.id/wp-content/uploads/2018/07/logo-NAM-air.png","Denpasar","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Nam Air", 2817150, "17.45", "1.25", "http://inaca.or.id/wp-content/uploads/2018/07/logo-NAM-air.png","Denpasar","Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 2369100, "7.00", "13.05", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Denpasar", "Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 2470100, "8.00", "15.05", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Denpasar", "Makasar", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air", 835100, "7.00", "8.45", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Padang", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Super Air Jet", 862300, "17.00", "18.45", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Padang", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 863344, "6.30", "8.20", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Padang", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],  
    ["Batik Air", 897900, "6.00", "7.45", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Padang", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Air Asia", 920000, "7.05", "8.50", "https://awards.brandingforum.org/wp-content/uploads/2016/05/airasia-feat-logo.jpg","Jakarta","Padang", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Garuda Indonesia", 1922100, "10.00", "11.50", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Padang", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 2711500, "6.00", "7.45", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Padang", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 2811500, "9.00", "10.45", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Padang", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 2711500, "16.20", "18.05", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Padang", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 4841400, "10.00", "11.50", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Padang", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 2281800, "16.30", "21.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 2665430, "19.15", "10.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Surabaya","Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],  
    ["Super Air Jet", 2120100, "6.00", "11.05", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Surabaya","Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Super Air Jet", 2499800, "6.00", "12.20", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Surabaya","Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 2611500, "5.00", "12.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 6675200, "9.10", "14.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 8617700, "9.10", "14.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 13342200, "7.00", "13.35", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Surabaya","Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"First"],
    ["Garuda Indonesia", 13342200, "7.00", "16.00", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Surabaya","Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"First"],
    ["Garuda Indonesia", 13342200, "12.00", "21.00", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Surabaya","Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"First"],
    ["Super Air Jet", 1030500, "17.45", "20.05", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Super Air Jet", 1115900, "8.45", "11.05", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air", 1088700, "10.30", "12.50", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Air Asia", 1143900, "9.55", "12.10", "https://awards.brandingforum.org/wp-content/uploads/2016/05/airasia-feat-logo.jpg","Jakarta","Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 1200229, "18.15", "20.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],  
    ["Batik Air", 3285600, "6.00", "8.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 3285600, "7.00", "9.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 3285600, "8.00", "10.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 5241000, "11.10", "13.35", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 5241000, "13.35", "16.00", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Medan", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Super Air Jet", 575200, "7.00", "8.05", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Palembang", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air", 599000, "8.00", "9.05", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Palembang", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Sriwijaya Air", 813580, "15.20", "10.10", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Jakarta","Palembang", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 1589100, "5.30", "6.35", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Palembang", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 4620400, "13.50", "15.00", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Palembang", (datetime.now()+timedelta()).strftime("%d %B %Y"),"First"],
    ["Lion Air",1301100, "6.30", "9.30", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJzv4qYKK5-q0QCjrI6bVDoQ9bgZehhuZNKYndCOz0N2V8dU0&s","Yogyakarta","Bali", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"], 
    ["Citilink", 1515300, "4.00", "5.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],  
    ["Citilink", 3448900, "5.00", "6.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],  
    ["Citilink", 5509500, "6.00", "7.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Yogyakarta","Bali", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],  
    ["Citilink", 1828300, "16.40", "19.40", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Yogyakarta","Bali", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 5509500, "18.00", "19.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Aceh","Riau", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 1500000, "7.30", " 9.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Surabaya", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 3000000, "8.30", "10.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Surabaya", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 1500000, "9.30", "11.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Aceh","Riau", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 1500000, "7.30", "9.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Yogyakarta","Bali", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Batavia Air", 1250000, "13.00", "14.30", "https://img.okezone.com/content/2013/01/30/320/754223/QtNnEhwvcc.jpg","Yogyakarta","Bali", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    ["Batavia Air", 2900000, "15.00", "16.30", "https://img.okezone.com/content/2013/01/30/320/754223/QtNnEhwvcc.jpg","Aceh","Riau", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Batavia Air", 3000000, "17.00", "18.15", "https://img.okezone.com/content/2013/01/30/320/754223/QtNnEhwvcc.jpg","Aceh","Riau", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Bisnis"],
    ["Wings Air", 1400000, "10.00", "11.30", "https://i.pinimg.com/originals/54/f0/dc/54f0dc6dd428e188136c16de7ffdb6bf.png","Aceh","Riau", (datetime.now()+timedelta()).strftime("%d %B %Y"),"Ekonomi"],
    
    ["Lion Air",1301100, "4.00", "5.30", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Surabaya", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air",1515300, "5.00", "6.30", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Surabaya", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air",3448900, "6.00", "7.30", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Surabaya", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 5509500, "6.30", " 8.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 5509500, "8.00", "9.30", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia",6426500, "10.30", "12.00", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Surabaya", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia",1828300, "13.00", "14.30", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Surabaya", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 1515300, "18.00", "19.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],  
    ["Citilink", 5509500, "19.00", "20.40", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Bisnis"],  
    ["Citilink", 5500000, "16.40", "19.40", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Bisnis"],
    ["Citilink", 7509500, "19.00", "20.40", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"First"],  
    ["Citilink", 7500000, "16.40", "19.40", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"First"],  
    ["Batik Air", 2424500, "9.00", "11.05", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya","Bali", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 9552500, "11.00", "13.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya","Bali", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Bisnis"],
    ["Air Asia", 641200, "15.30", "17.25", "https://awards.brandingforum.org/wp-content/uploads/2016/05/airasia-feat-logo.jpg","Surabaya","Bali", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],
    ["Air Asia", 650000, "17.00", "19.00", "https://awards.brandingforum.org/wp-content/uploads/2016/05/airasia-feat-logo.jpg","Surabaya","Bali", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Sriwijaya Air", 2708000, "17.30", "19.20", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Surabaya","Bali", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Nam Air", 1424960, "18.50", "21.40", "http://inaca.or.id/wp-content/uploads/2018/07/logo-NAM-air.png","Jakarta","Bali", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Air Asia", 1486900, "16.25", "19.15", "https://awards.brandingforum.org/wp-content/uploads/2016/05/airasia-feat-logo.jpg","Jakarta","Bali", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Ekonomi"],
    ["Sriwijaya Air", 2708000, "17.30", "19.20", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Jakarta","Bali", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 4220600, "6.30", " 9.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Bali", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 6602600, "4.30", " 7.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Bali", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 6761900, "9.10", "12.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Banjarmasim", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 6761900, "15.00", "17.50", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Banjarmasim", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 5907000, "13.00", "15.50", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Banjarmasim", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 10151400, "5.00", "12.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Banjarmasim", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 14363400, "7.00", "15.50", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Surabaya","Banjarmasim", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 1875400, "14.10", "18.30", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Pontianak", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 1875400, "19.00", "23.10", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Pontianak", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 5774200, "19.00", "23.10", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Pontianak", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 11444100, "18.40", "23.00", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Surabaya","Pontianak", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Bisnis"],
    ["Lion Air", 862200, "17.00", "18.30", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Pontianak", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air", 862200, "19.00", "20.30", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Pontianak", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],
    ["Super Air Jet", 889400, "17.00", "18.30", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Pontianak", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Super Air Jet", 889200, "20.00", "21.30", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Pontianak", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 3818800, "15.30", "17.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Pontianak", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 3818800, "16.00", "17.30", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Pontianak", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Bisnis"],
    ["Super Air Jet", 1290300, "4.45", "8.10", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Makasar", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Ekonomi"],
    ["Sriwijaya Air", 1398320, "13.35", "17.00", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Jakarta","Makasar", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 1972655, "14.00", "17.25", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Makasar", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],  
    ["Sriwijaya Air", 2060990, "22.00", "1.25", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Jakarta","Makasar", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],
    ["Garuda Indonesia", 2366100, "22.05", "1.30", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Makasar", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],
    ["Garuda Indonesia", 4530600, "1.30", "5.05", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Makasar", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 7261200, "15.10", "18.45", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Makasar", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"First"],
    ["Garuda Indonesia", 4530600, "22.05", "1.25", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Makasar", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 3340100, "5.30", "8.55", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Pontianak", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 3340100, "9.40", "13.05", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Pontianak", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Bisnis"],
    ["Citilink", 1307681, "6.00", "8.25", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Surabaya","Makasar", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Ekonomi"],  
    ["Citilink", 1430681, "6.00", "8.25", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Surabaya","Makasar", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],  
    ["Lion Air", 1272100, "16.20", "18.50", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Surabaya","Makasar", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],
    ["Sriwijaya Air", 1486900, "19.20", "21.50", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Surabaya","Makasar", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],
    ["Sriwijaya Air", 1486900, "19.50", "22.20", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Surabaya","Makasar", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 2427900, "5.00", "7.30", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Makasar", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 6729700, "5.00", "7.30", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Makasar", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"First"],
    ["Batik Air", 7510600, "7.00", "13.05", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Denpasar", "Makasar", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 13105900, "19.25", "1.25", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Denpasar","Makasar", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"First"],
    ["Garuda Indonesia", 13105900, "18.40", "1.25", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Denpasar","Makasar", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"First"],
    ["Garuda Indonesia", 13105900, "19.25", "7.40", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Denpasar","Makasar", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"First"],
    ["Lion Air", 1906400, "8.35", "12.50", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Denpasar","Makasar", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air", 1226400, "12.10", "13.30", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Denpasar","Makasar", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 1312337, "15.30", "17.00", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Denpasar","Makasar", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],  
    ["Sriwijaya Air", 1019720, "19.25", "20.45", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Denpasar","Makasar", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Nam Air", 2010190, "17.45", "19.00", "http://inaca.or.id/wp-content/uploads/2018/07/logo-NAM-air.png","Denpasar","Makasar", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Nam Air", 2817150, "17.45", "1.25", "http://inaca.or.id/wp-content/uploads/2018/07/logo-NAM-air.png","Denpasar","Makasar", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 2369100, "7.00", "13.05", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Denpasar", "Makasar", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 2470100, "8.00", "15.05", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Denpasar", "Makasar", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air", 835100, "7.00", "8.45", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Padang", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],
    ["Super Air Jet", 862300, "17.00", "18.45", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Padang", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 863344, "6.30", "8.20", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Padang", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],  
    ["Batik Air", 897900, "6.00", "7.45", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Padang", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Air Asia", 920000, "7.05", "8.50", "https://awards.brandingforum.org/wp-content/uploads/2016/05/airasia-feat-logo.jpg","Jakarta","Padang", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Garuda Indonesia", 1922100, "10.00", "11.50", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Padang", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 2711500, "6.00", "7.45", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Padang", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 2811500, "9.00", "10.45", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Padang", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 2711500, "16.20", "18.05", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Padang", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 4841400, "10.00", "11.50", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Padang", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 2281800, "16.30", "21.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Medan", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 2665430, "19.15", "10.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Surabaya","Medan", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],  
    ["Super Air Jet", 2120100, "6.00", "11.05", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Surabaya","Medan", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Super Air Jet", 2499800, "6.00", "12.20", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Surabaya","Medan", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 2611500, "5.00", "12.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Medan", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 6675200, "9.10", "14.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Medan", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 8617700, "9.10", "14.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Medan", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 13342200, "7.00", "13.35", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Surabaya","Medan", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"First"],
    ["Garuda Indonesia", 13342200, "7.00", "16.00", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Surabaya","Medan", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"First"],
    ["Garuda Indonesia", 13342200, "12.00", "21.00", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Surabaya","Medan", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"First"],
    ["Super Air Jet", 1030500, "17.45", "20.05", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Medan", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],
    ["Super Air Jet", 1115900, "8.45", "11.05", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Medan", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air", 1088700, "10.30", "12.50", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Medan", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Air Asia", 1143900, "9.55", "12.10", "https://awards.brandingforum.org/wp-content/uploads/2016/05/airasia-feat-logo.jpg","Jakarta","Medan", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 1200229, "18.15", "20.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Medan", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Ekonomi"],  
    ["Batik Air", 3285600, "6.00", "8.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Medan", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 3285600, "7.00", "9.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Medan", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 3285600, "8.00", "10.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Medan", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 5241000, "11.10", "13.35", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Medan", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 5241000, "13.35", "16.00", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Medan", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Bisnis"],
    ["Super Air Jet", 575200, "7.00", "8.05", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Palembang", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air", 599000, "8.00", "9.05", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Palembang", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Sriwijaya Air", 813580, "15.20", "10.10", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Jakarta","Palembang", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 1589100, "5.30", "6.35", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Palembang", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 4620400, "13.50", "15.00", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Palembang", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"First"],
    ["Lion Air",1301100, "6.30", "9.30", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJzv4qYKK5-q0QCjrI6bVDoQ9bgZehhuZNKYndCOz0N2V8dU0&s","Yogyakarta","Bali", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Ekonomi"], 
    ["Citilink", 1515300, "4.00", "5.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],  
    ["Citilink", 3448900, "5.00", "6.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Bisnis"],  
    ["Citilink", 5509500, "6.00", "7.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Yogyakarta","Bali", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Bisnis"],  
    ["Citilink", 1828300, "16.40", "19.40", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Yogyakarta","Bali", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 5509500, "18.00", "19.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Aceh","Riau", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 1500000, "7.30", " 9.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 3000000, "8.30", "10.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 1500000, "9.30", "11.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Aceh","Riau", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 1500000, "7.30", "9.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Yogyakarta","Bali", (datetime.now()+timedelta(1)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batavia Air", 1250000, "13.00", "14.30", "https://img.okezone.com/content/2013/01/30/320/754223/QtNnEhwvcc.jpg","Yogyakarta","Bali", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batavia Air", 2900000, "15.00", "16.30", "https://img.okezone.com/content/2013/01/30/320/754223/QtNnEhwvcc.jpg","Aceh","Riau", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Bisnis"],
    ["Batavia Air", 3000000, "17.00", "18.15", "https://img.okezone.com/content/2013/01/30/320/754223/QtNnEhwvcc.jpg","Aceh","Riau", (datetime.now()+timedelta(2)).strftime("%d %B %Y"),"Bisnis"],
    ["Wings Air", 1400000, "10.00", "11.30", "https://i.pinimg.com/originals/54/f0/dc/54f0dc6dd428e188136c16de7ffdb6bf.png","Aceh","Riau", (datetime.now()+timedelta(3)).strftime("%d %B %Y"),"Ekonomi"],
    
     ["Lion Air",1301100, "4.00", "5.30", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Surabaya", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air",1515300, "5.00", "6.30", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Surabaya", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air",3448900, "6.00", "7.30", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Surabaya", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 5509500, "6.30", " 8.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 5509500, "8.00", "9.30", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia",6426500, "10.30", "12.00", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Surabaya", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia",1828300, "13.00", "14.30", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Surabaya", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 1515300, "18.00", "19.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],  
    ["Citilink", 5509500, "19.00", "20.40", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Bisnis"],  
    ["Citilink", 5500000, "16.40", "19.40", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Bisnis"],
    ["Citilink", 7509500, "19.00", "20.40", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"First"],  
    ["Citilink", 7500000, "16.40", "19.40", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"First"],  
    ["Batik Air", 2424500, "9.00", "11.05", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya","Bali", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 9552500, "11.00", "13.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya","Bali", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Bisnis"],
    ["Air Asia", 641200, "15.30", "17.25", "https://awards.brandingforum.org/wp-content/uploads/2016/05/airasia-feat-logo.jpg","Surabaya","Bali", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],
    ["Air Asia", 650000, "17.00", "19.00", "https://awards.brandingforum.org/wp-content/uploads/2016/05/airasia-feat-logo.jpg","Surabaya","Bali", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Sriwijaya Air", 2708000, "17.30", "19.20", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Surabaya","Bali", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Nam Air", 1424960, "18.50", "21.40", "http://inaca.or.id/wp-content/uploads/2018/07/logo-NAM-air.png","Jakarta","Bali", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Air Asia", 1486900, "16.25", "19.15", "https://awards.brandingforum.org/wp-content/uploads/2016/05/airasia-feat-logo.jpg","Jakarta","Bali", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Ekonomi"],
    ["Sriwijaya Air", 2708000, "17.30", "19.20", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Jakarta","Bali", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 4220600, "6.30", " 9.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Bali", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 6602600, "4.30", " 7.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Bali", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 6761900, "9.10", "12.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Banjarmasim", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 6761900, "15.00", "17.50", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Banjarmasim", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 5907000, "13.00", "15.50", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Banjarmasim", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 10151400, "5.00", "12.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Banjarmasim", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 14363400, "7.00", "15.50", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Surabaya","Banjarmasim", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 1875400, "14.10", "18.30", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Pontianak", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 1875400, "19.00", "23.10", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Pontianak", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 5774200, "19.00", "23.10", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Pontianak", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 11444100, "18.40", "23.00", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Surabaya","Pontianak", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Bisnis"],
    ["Lion Air", 862200, "17.00", "18.30", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Pontianak", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air", 862200, "19.00", "20.30", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Pontianak", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],
    ["Super Air Jet", 889400, "17.00", "18.30", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Pontianak", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Super Air Jet", 889200, "20.00", "21.30", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Pontianak", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 3818800, "15.30", "17.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Pontianak", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 3818800, "16.00", "17.30", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Pontianak", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Bisnis"],
    ["Super Air Jet", 1290300, "4.45", "8.10", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Makasar", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Ekonomi"],
    ["Sriwijaya Air", 1398320, "13.35", "17.00", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Jakarta","Makasar", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 1972655, "14.00", "17.25", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Makasar", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],  
    ["Sriwijaya Air", 2060990, "22.00", "1.25", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Jakarta","Makasar", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],
    ["Garuda Indonesia", 2366100, "22.05", "1.30", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Makasar", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],
    ["Garuda Indonesia", 4530600, "1.30", "5.05", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Makasar", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 7261200, "15.10", "18.45", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Makasar", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"First"],
    ["Garuda Indonesia", 4530600, "22.05", "1.25", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Makasar", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 3340100, "5.30", "8.55", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Pontianak", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 3340100, "9.40", "13.05", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Pontianak", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Bisnis"],
    ["Citilink", 1307681, "6.00", "8.25", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Surabaya","Makasar", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Ekonomi"],  
    ["Citilink", 1430681, "6.00", "8.25", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Surabaya","Makasar", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],  
    ["Lion Air", 1272100, "16.20", "18.50", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Surabaya","Makasar", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],
    ["Sriwijaya Air", 1486900, "19.20", "21.50", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Surabaya","Makasar", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],
    ["Sriwijaya Air", 1486900, "19.50", "22.20", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Surabaya","Makasar", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 2427900, "5.00", "7.30", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Makasar", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 6729700, "5.00", "7.30", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Makasar", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"First"],
    ["Batik Air", 7510600, "7.00", "13.05", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Denpasar", "Makasar", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 13105900, "19.25", "1.25", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Denpasar","Makasar", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"First"],
    ["Garuda Indonesia", 13105900, "18.40", "1.25", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Denpasar","Makasar", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"First"],
    ["Garuda Indonesia", 13105900, "19.25", "7.40", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Denpasar","Makasar", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"First"],
    ["Lion Air", 1906400, "8.35", "12.50", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Denpasar","Makasar", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air", 1226400, "12.10", "13.30", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Denpasar","Makasar", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 1312337, "15.30", "17.00", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Denpasar","Makasar", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],  
    ["Sriwijaya Air", 1019720, "19.25", "20.45", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Denpasar","Makasar", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Nam Air", 2010190, "17.45", "19.00", "http://inaca.or.id/wp-content/uploads/2018/07/logo-NAM-air.png","Denpasar","Makasar", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Nam Air", 2817150, "17.45", "1.25", "http://inaca.or.id/wp-content/uploads/2018/07/logo-NAM-air.png","Denpasar","Makasar", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 2369100, "7.00", "13.05", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Denpasar", "Makasar", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 2470100, "8.00", "15.05", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Denpasar", "Makasar", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air", 835100, "7.00", "8.45", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Padang", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],
    ["Super Air Jet", 862300, "17.00", "18.45", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Padang", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 863344, "6.30", "8.20", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Padang", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],  
    ["Batik Air", 897900, "6.00", "7.45", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Padang", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Air Asia", 920000, "7.05", "8.50", "https://awards.brandingforum.org/wp-content/uploads/2016/05/airasia-feat-logo.jpg","Jakarta","Padang", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Garuda Indonesia", 1922100, "10.00", "11.50", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Padang", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 2711500, "6.00", "7.45", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Padang", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 2811500, "9.00", "10.45", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Padang", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 2711500, "16.20", "18.05", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Padang", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 4841400, "10.00", "11.50", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Padang", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 2281800, "16.30", "21.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Medan", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 2665430, "19.15", "10.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Surabaya","Medan", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],  
    ["Super Air Jet", 2120100, "6.00", "11.05", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Surabaya","Medan", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Super Air Jet", 2499800, "6.00", "12.20", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Surabaya","Medan", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 2611500, "5.00", "12.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Medan", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 6675200, "9.10", "14.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Medan", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 8617700, "9.10", "14.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Surabaya", "Medan", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 13342200, "7.00", "13.35", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Surabaya","Medan", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"First"],
    ["Garuda Indonesia", 13342200, "7.00", "16.00", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Surabaya","Medan", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"First"],
    ["Garuda Indonesia", 13342200, "12.00", "21.00", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Surabaya","Medan", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"First"],
    ["Super Air Jet", 1030500, "17.45", "20.05", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Medan", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],
    ["Super Air Jet", 1115900, "8.45", "11.05", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Medan", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air", 1088700, "10.30", "12.50", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Medan", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Air Asia", 1143900, "9.55", "12.10", "https://awards.brandingforum.org/wp-content/uploads/2016/05/airasia-feat-logo.jpg","Jakarta","Medan", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 1200229, "18.15", "20.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Medan", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Ekonomi"],  
    ["Batik Air", 3285600, "6.00", "8.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Medan", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 3285600, "7.00", "9.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta", "Medan", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 3285600, "8.00", "10.20", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Medan", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 5241000, "11.10", "13.35", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Medan", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 5241000, "13.35", "16.00", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Medan", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Bisnis"],
    ["Super Air Jet", 575200, "7.00", "8.05", 'https://1.bp.blogspot.com/-9_y2tzAapOY/YWu2lxJ_q4I/AAAAAAAADeU/ybIUDvt-Gnk2sDQupGIQW26KOif_WBWeQCNcBGAsYHQ/s2048/Super%2BAir%2BJet.png',"Jakarta","Palembang", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Lion Air", 599000, "8.00", "9.05", 'https://logos-download.com/wp-content/uploads/2016/05/Lion_Air_logo_logotype.png',"Jakarta","Palembang", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Sriwijaya Air", 813580, "15.20", "10.10", "https://i.pinimg.com/originals/8c/e2/55/8ce2559b2ea024a918bae0d19f2e2907.jpg","Jakarta","Palembang", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 1589100, "5.30", "6.35", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Palembang", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Bisnis"],
    ["Garuda Indonesia", 4620400, "13.50", "15.00", 'https://1.bp.blogspot.com/-7GZE8e5zNuY/YWu4HNMnquI/AAAAAAAADek/CpIzS-i9gik4lB3ESPm5OxBVWNKmC0RawCNcBGAsYHQ/s2048/Garuda%2BIndonesia.png',"Jakarta","Palembang", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"First"],
    ["Lion Air",1301100, "6.30", "9.30", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJzv4qYKK5-q0QCjrI6bVDoQ9bgZehhuZNKYndCOz0N2V8dU0&s","Yogyakarta","Bali", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Ekonomi"], 
    ["Citilink", 1515300, "4.00", "5.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],  
    ["Citilink", 3448900, "5.00", "6.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Bisnis"],  
    ["Citilink", 5509500, "6.00", "7.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Yogyakarta","Bali", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Bisnis"],  
    ["Citilink", 1828300, "16.40", "19.40", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Yogyakarta","Bali", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Citilink", 5509500, "18.00", "19.30", "https://i.pinimg.com/236x/16/3e/e3/163ee3ef17959b0b2e4b88ae590ff9a5.jpg","Aceh","Riau", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 1500000, "7.30", " 9.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 3000000, "8.30", "10.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Jakarta","Surabaya", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Bisnis"],
    ["Batik Air", 1500000, "9.30", "11.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Aceh","Riau", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batik Air", 1500000, "7.30", "9.00", "https://airmundo.com/app/uploads/2019/05/Batik-Air-brand-logo-400x240.jpg","Yogyakarta","Bali", (datetime.now()+timedelta(4)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batavia Air", 1250000, "13.00", "14.30", "https://img.okezone.com/content/2013/01/30/320/754223/QtNnEhwvcc.jpg","Yogyakarta","Bali", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Ekonomi"],
    ["Batavia Air", 2900000, "15.00", "16.30", "https://img.okezone.com/content/2013/01/30/320/754223/QtNnEhwvcc.jpg","Aceh","Riau", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Bisnis"],
    ["Batavia Air", 3000000, "17.00", "18.15", "https://img.okezone.com/content/2013/01/30/320/754223/QtNnEhwvcc.jpg","Aceh","Riau", (datetime.now()+timedelta(5)).strftime("%d %B %Y"),"Bisnis"],
    ["Wings Air", 1400000, "10.00", "11.30", "https://i.pinimg.com/originals/54/f0/dc/54f0dc6dd428e188136c16de7ffdb6bf.png","Aceh","Riau", (datetime.now()+timedelta(6)).strftime("%d %B %Y"),"Ekonomi"]]


#buat list    
mylist=ep.copy()
mylist2=[] #dari
for i in range(len(mylist)):
    mylist2.append(mylist[i][5])
mylist2 = list(dict.fromkeys(mylist2))

mylist3=[] #tujuan
for i in range(len(mylist)):
	mylist3.append(mylist[i][6])
mylist3 = list(dict.fromkeys(mylist3))
#kenapa ini ketuker
mylist4=[] #Kelas
for i in range(len(mylist)):
	mylist4.append(mylist[i][8])
mylist4 = list(dict.fromkeys(mylist4))

mylist5=[] #tanggal
for i in range(len(mylist)):
	mylist5.append(mylist[i][7])
mylist5 = list(dict.fromkeys(mylist5))
ditampilkan=[] #apanya


class ContentCustomSheet():
    pass
    # def Lang(self):
    #     snackbar = Snackbar(text="find the plane you need!!!",snackbar_x="10dp",snackbar_y="10dp",radius=[20,20,20,20])
    #     snackbar.size_hint_x = (Window.width - (snackbar.snackbar_x * 2)) / Window.width
    #     snackbar.buttons = [MDFlatButton(text="[color=#fafafa]OK[/color]",on_release=snackbar.dismiss)]
    #     snackbar.open()
        
class Maine(Screen):
    def callback(self, button):
        snackbar = Snackbar(text="find the plane you need!!!",snackbar_x="10dp",snackbar_y="10dp",radius=[20,20,20,20])
        snackbar.size_hint_x = (Window.width - (snackbar.snackbar_x * 2)) / Window.width
        snackbar.buttons = [MDFlatButton(text="[color=#fafafa]OK[/color]",on_release=snackbar.dismiss)]
        snackbar.open()
    def bueck(self):
        screen_manager.get_screen('maine').ids.video_list.clear_widgets()
        screen_manager.current = "Pesawat"
    def open_bottom_sheet(self):
        bottom_sheet_menu = MDListBottomSheet(radius_from="top", radius=25)
        menu_items = [
            ("Sort by price (Buble Sort)", lambda x: self.oyu(1,1), "price.png"), 
            ("Sort by earliest departure (Buble Sort)", lambda x: self.oyu(1,2), "departure.png"),
            ("Sort by earliest arrival (Buble Sort)", lambda x: self.oyu(1,3), "arrival.png"),
            ("Sort by price (Selection Sort)", lambda x: self.oyu(2,1), "price.png"),
            ("Sort by earliest departure (Selection Sort)", lambda x: self.oyu(2,2), "departure.png"),
            ("Sort by earliest arrival (Selection Sort)", lambda x: self.oyu(2,3), "arrival.png"),
            ("Sort by price (Insertion Sort)", lambda x: self.oyu(3,1), "price.png"),
            ("Sort by earliest departure (Insertion Sort)", lambda x: self.oyu(3,2), "departure.png"),
            ("Sort by earliest arrival (Insertion Sort)", lambda x: self.oyu(3,3), "arrival.png"),
            ("Sort by price (Merge Sort)", lambda x: self.oyu(4,1), "price.png"),
            ("Sort by earliest departure (Merge Sort)", lambda x: self.oyu(4,2), "departure.png"),
            ("Sort by earliest arrival (Merge Sort)", lambda x: self.oyu(4,3), "arrival.png"),
            ("Help", lambda x: self.callback(x), "help"),
            ("Cancel", lambda x: bottom_sheet_menu.dismiss(), "close"),

        ]
        for txt, func, icon in menu_items:
            bottom_sheet_menu.add_item(txt, func, icon)
        bottom_sheet_menu.open()
    def oyu(self,sort,sortby):
        global ditampilkan 
        screen_id = screen_manager.get_screen('maine').ids.video_list 
        screen_id.clear_widgets() 
        if len(ditampilkan) == 0:
            screen_id.add_widget(MDLabel(text= f"not found",theme_text_color = "Secondary",halign= 'center', pos_hint={'center_x': .5, 'center_y': .5}, valign= 'center'))
        if sort == 1: #Bubble
            for i in range(len(ditampilkan)):
                for j in range(0, len(ditampilkan) - i - 1):
                    if float(ditampilkan[j][sortby]) > float(ditampilkan[j + 1][sortby]):
                        temp = ditampilkan[j]
                        ditampilkan[j] = ditampilkan[j+1]
                        ditampilkan[j+1] = temp
            screen_id.add_widget(MDLabel(text="Hasil Algoritma Bubble", theme_text_color="Primary"))
        if sort == 2: #Selection
            for step in range(len(ditampilkan)):
                min_idx = step
                for i in range(step + 1, len(ditampilkan)):
                    if float(ditampilkan[i][sortby]) < float(ditampilkan[min_idx][sortby]):
                        min_idx = i
                (ditampilkan[step], ditampilkan[min_idx]) = (ditampilkan[min_idx], ditampilkan[step])
            screen_id.add_widget(MDLabel(text="Hasil Algoritma Selection", theme_text_color="Primary"))
        if sort == 3: #Insertionn
            array=ditampilkan
            for step in range(1, len(array)):
                key = array[step]
                j = step - 1      
                while j >= 0 and float(key[sortby]) < float(array[j][sortby]):
                    array[j + 1] = array[j]
                    j = j - 1
                array[j + 1] = key
            screen_id.add_widget(MDLabel(text="Hasil Algoritma Insertion", theme_text_color="Primary"))
        if sort == 4: #merge
            def mergeSort(array):
                if len(array) > 1:
                    r = len(array)//2
                    L = array[:r]
                    M = array[r:]
                    mergeSort(L) 
                    mergeSort(M) 
                    i = j = k = 0
                    while i < len(L) and j < len(M):
                        if float(L[i][sortby]) < float(M[j][sortby]):
                            array[k] = L[i]
                            i += 1
                        else:
                            array[k] = M[j]
                            j += 1
                        k += 1
                    while i < len(L):
                        array[k] = L[i]
                        i += 1
                        k += 1
                    while j < len(M):
                        array[k] = M[j]
                        j += 1
                        k += 1
            mergeSort(ditampilkan)
        for i in range(len(ditampilkan)):
            image = AsyncImage(source= ditampilkan[i][4], size_hint=(1, 1)) #async ambil dari internet
            card = MDCard(orientation = 'horizontal',pos_hint={'center_x': .5, 'center_y': .5}, size_hint = (.95,None), size = (self.width, dp(120)) , ripple_behavior = True, padding = [0,0,dp(8),0], radius = 30, elevation = 10)
            def cekout():
                global ditampilkan
                bottom_sheet_menu2 = MDCustomBottomSheet(screen=Factory.ContentCustomSheet())		
                bottom_sheet_menu2.open()
            card.bind(on_release = lambda x:cekout())
            isicard1 = MDBoxLayout(size = (dp(120) , dp(120)), size_hint = (None, None), pos_hint = {"center_x": .5, "center_y": .5})
            isicard2 = MDBoxLayout(orientation="vertical", size = (self.width, dp(120)),size_hint = (.95,None))
            penerbangan = MDLabel(text= str(ditampilkan[i][0]),theme_text_color = "Primary",)#size_hint = (.95,None), size = (self.width, dp(120))) #'''size_hint_y = None''')
            lines= MDSeparator(height=dp(1))
            jam = MDLabel(text= f"{str(ditampilkan[i][2])}-{str(ditampilkan[i][3])}",theme_text_color = "Secondary")#, size_hint_y = None)
            harga = MDLabel(text= "IDR " + str(ditampilkan[i][1]),theme_text_color = "Secondary",halign="right",)# size_hint_y = None)
            card.add_widget(isicard1)
            card.add_widget(isicard2)
            isicard1.add_widget(image)
            isicard2.add_widget(penerbangan)
            isicard2.add_widget(lines)
            isicard2.add_widget(jam)
            isicard2.add_widget(harga)
            screen_id.add_widget(card)

class MainScreen(Screen):
	def callback(self):
		snackbar = Snackbar(text="coming soon!!!",snackbar_x="10dp",snackbar_y="10dp",radius=[20,20,20,20])
		snackbar.size_hint_x = (Window.width - (snackbar.snackbar_x * 2)) / Window.width
		snackbar.buttons = [MDFlatButton(text="[color=#fafafa]OK[/color]",on_release=snackbar.dismiss)]
		snackbar.open()
	def ToPesawat(self):
		screen_manager.current = "Pesawat"
	def tochat(self):
		screen_manager.current = "chats"

class Sortp(Screen):
    def callback(self, button):
        Snackbar(text="Coming Soon!!!").open()
    def bueck(self):
        screen_manager.current = "Pesawat"
    def oyu(self):
        card.clear_widgets()
		
class IconListItem(OneLineIconListItem):
    icon = StringProperty()
    
class Chatcus(Screen):
    def jawaban(self, dt):
        rendem=["okay","hmmm","iya","baik","siap",'pesawat?']
        oooo = MDCard(orientation = 'horizontal',pos_hint={'center_x': .4, 'center_y': .5}, size_hint = (.7,None) , ripple_behavior = True, padding = [0,0,dp(8),0], radius = [40,40,40,0], elevation = 10)
        kamu=MDLabel(text=random.choice(rendem),size_hint_y= None,pos_hint= {"x": .02}, padding= (12, 10), theme_text_color= "Custom", text_color= (0, 0, 0, 1))
        oooo.add_widget(kamu)
        screen_manager.get_screen('chats').chat_list.add_widget(oooo)
    def bueck(self):
        screen_manager.current = "MainScreen"
    def send(self):
        ooo = MDCard(orientation = 'horizontal',pos_hint={'center_x': .6, 'center_y': .5}, size_hint = (.7,None) , ripple_behavior = True, padding = [0,0,dp(8),0], radius = [40,40,0,40], elevation = 10,md_bg_color=get_color_from_hex("#A4B3E2") )
        aku=MDLabel(text= screen_manager.get_screen('chats').text_input.text, size_hint_y= None,pos_hint= {"x": .98}, padding= (12, 10), theme_text_color= "Custom", text_color= (1, 1, 1, 1))
        ooo.add_widget(aku)
        screen_manager.get_screen('chats').chat_list.add_widget(ooo)
        Clock.schedule_once(self.jawaban, 1.5)
        screen_manager.get_screen('chats').text_input.text = ""

class Pesawat(Screen):
    def display_date(self):
        # Create the drop down menu
        menu_items4 = [
            {
                "viewclass": "IconListItem",
                "icon": "calendar",
                "height": dp(56),
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.set_item4(x),
            } for i in mylist5]
        self.menu = MDDropdownMenu(
            caller=self.ids.dest_dropdown_item4,
            items=menu_items4,
            position="bottom",
            width_mult=4,
            radius=[40, 40, 40, 40],
        )
        self.menu.open()
        self.menu.bind(on_release=self.set_item)
    def display_class(self):
        # Create the drop down menu
        menu_items3 = [
            {
                "viewclass": "IconListItem",
                "icon": "crown-outline",
                "height": dp(56),
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.set_item3(x),
            } for i in mylist4]
        self.menu = MDDropdownMenu(
            caller=self.ids.dest_dropdown_item3,
            items=menu_items3,
            position="bottom",
            width_mult=4,
            radius=[40, 40, 40, 40],
        )
        self.menu.open()
        self.menu.bind(on_release=self.set_item)
    def display_arrival(self):
        # Create the drop down menu
        menu_items2 = [
            {
                "viewclass": "IconListItem",
                "icon": "arrival.png",
                "height": dp(56),
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.set_item2(x),
            } for i in mylist3]
        self.menu = MDDropdownMenu(
            caller=self.ids.dest_dropdown_item2,
            items=menu_items2,
            position="bottom",
            width_mult=4,
            radius=[40, 40, 40, 40],
        )
        self.menu.open()
        self.menu.bind(on_release=self.set_item)
    def display_departure(self):
        # Create the drop down menu
        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "departure.png",
                "height": dp(56),
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.set_item(x),
            } for i in mylist2]
        self.menu = MDDropdownMenu(
            caller=self.ids.dest_dropdown_item,
            items=menu_items,
            position="bottom",
            width_mult=4,
            radius=[40, 40, 40, 40],
        )
        self.menu.open()
        self.menu.bind(on_release=self.set_item)
    def set_item3(self, instance_menu_item):
        self.ids.dest_dropdown_item3.text = instance_menu_item
        self.menu.dismiss()
    def set_item4(self, instance_menu_item):
        self.ids.dest_dropdown_item4.text = instance_menu_item
        self.menu.dismiss()
    def set_item2(self, instance_menu_item):
        self.ids.dest_dropdown_item2.text = instance_menu_item
        self.menu.dismiss()
    def set_item(self, instance_menu_item):
        self.ids.dest_dropdown_item.text = instance_menu_item
        self.menu.dismiss()
    def callback(self, button):
        snackbar = Snackbar(text="complete the search index!!!",snackbar_x="10dp",snackbar_y="10dp",radius=[20,20,20,20])
        snackbar.size_hint_x = (Window.width - (snackbar.snackbar_x * 2)) / Window.width
        snackbar.buttons = [MDFlatButton(text="[color=#fafafa]OK[/color]",on_release=snackbar.dismiss)]
        snackbar.open()
    def bueck(self):
        screen_manager.current = "MainScreen"
    def oyu(self):
        card.clear_widgets()
    def tosortp(self):
        if self.ids.dest_dropdown_item.text=="" or self.ids.dest_dropdown_item2.text=="" or self.ids.dest_dropdown_item3.text=="" or self.ids.dest_dropdown_item4.text=="":
            snackbar = Snackbar(text="complete the search index!!!",snackbar_x="10dp",snackbar_y="10dp",radius=[20,20,20,20])
            snackbar.size_hint_x = (Window.width - (snackbar.snackbar_x * 2)) / Window.width
            snackbar.buttons = [MDFlatButton(text="[color=#fafafa]OK[/color]",on_release=snackbar.dismiss)]
            snackbar.open()
            return
        screen_manager.current = "maine" #yang isinya list list pesawat
        screen_id = screen_manager.get_screen('maine').ids.video_list
        dari = self.ids.dest_dropdown_item.text
        ke = self.ids.dest_dropdown_item2.text
        tipe = self.ids.dest_dropdown_item3.text
        datet = self.ids.dest_dropdown_item4.text
        global ditampilkan
        ditampilkan.clear()
        for i in range(len(ep)):
            if dari == ep[i][5]:
                if ke == ep[i][6]:
                    if tipe == ep[i][8]:
                        if datet == ep[i][7]:
                            ditampilkan.append(ep[i])
        if len(ditampilkan) == 0:
            screen_id.add_widget(MDLabel(text= f"not found",theme_text_color = "Secondary",halign= 'center', pos_hint={'center_x': .5, 'center_y': .5}, valign= 'center'))
        for i in range(len(ditampilkan)):
            image = AsyncImage(source= ditampilkan[i][4], size_hint=(1, 1))
            global card
            card = MDCard(orientation = 'horizontal',pos_hint={'center_x': .5, 'center_y': .5}, size_hint = (.95,None), size = (self.width, dp(120)) , ripple_behavior = True, padding = [0,0,dp(8),0], radius = 30, elevation = 10)
            def cekout():
                global ditampilkan
                bottom_sheet_menu2 = MDCustomBottomSheet(screen=Factory.ContentCustomSheet())
                bottom_sheet_menu2.open()
            card.bind(on_release = lambda x:cekout())
            isicard1 = MDBoxLayout(size = (dp(120) , dp(120)), size_hint = (None, None), pos_hint = {"center_x": .5, "center_y": .5})
            isicard2 = MDBoxLayout(orientation="vertical", size = (self.width, dp(120)),size_hint = (.95,None))
            penerbangan = MDLabel(text= str(ditampilkan[i][0]),theme_text_color = "Primary",)#size_hint = (.95,None), size = (self.width, dp(120))) #'''size_hint_y = None''')
            lines= MDSeparator(height=dp(1))
            jam = MDLabel(text= f"{str(ditampilkan[i][2])}-{str(ditampilkan[i][3])}",theme_text_color = "Secondary")#, size_hint_y = None)
            harga = MDLabel(text= "IDR " + str(ditampilkan[i][1]),theme_text_color = "Secondary",halign="right",)# size_hint_y = None)
            card.add_widget(isicard1)
            card.add_widget(isicard2)
            isicard1.add_widget(image)
            isicard2.add_widget(penerbangan)
            isicard2.add_widget(lines)
            isicard2.add_widget(jam)
            isicard2.add_widget(harga)
            screen_id.add_widget(card)


class Walktr(Screen):
	def next(self):
		screen_manager.get_screen('walktr').ids.carousel.load_next(mode="next")
	def prev(self):
		screen_manager.get_screen('walktr').ids.carousel.load_previous()
	def tomen(self):
		screen_manager.current = "MainScreen"

class dws(MDApp):
    global screen_manager
    screen_manager = ScreenManager()
    def build(self):
        self.title=""
        screen_manager.add_widget(Builder.load_file("awww.kv"))
        #screen_manager.add_widget(OpeningScreen(name='OpeningScreen'))
        screen_manager.add_widget(MainScreen(name='MainScreen'))
        screen_manager.add_widget(Pesawat(name='Pesawat'))
        screen_manager.add_widget(Sortp(name='Sortp'))
        screen_manager.add_widget(Maine(name='maine'))
        screen_manager.add_widget(Walktr(name='walktr'))
        screen_manager.add_widget(Chatcus(name='chats'))
        
        return screen_manager
    def on_start(self):
        Clock.schedule_once(self.change_screen, 2)
    def change_screen(self, dt):    
        screen_manager.current = "walktr"
    def callback(self):
        snackbar = Snackbar(text="this fiture avaible soon",snackbar_x="10dp",snackbar_y="10dp",radius=[20,20,20,20])
        snackbar.size_hint_x = (Window.width - (snackbar.snackbar_x * 2)) / Window.width
        snackbar.buttons = [MDFlatButton(text="[color=#fafafa]OK[/color]",on_release=snackbar.dismiss)]
        snackbar.open()
        
dws().run()