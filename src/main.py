import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
import requests

kivy.require('2.0.0')


class CustomSpinnerOption(SpinnerOption):
    def __init__(self, **kwargs):
        super(CustomSpinnerOption, self).__init__(**kwargs)
        self.font_name = "Roboto-Regular"  
        self.font_size = '20sp'

class CustomSpinner(Spinner):
    def __init__(self, **kwargs):
        super(CustomSpinner, self).__init__(**kwargs)
        self.option_cls = CustomSpinnerOption
        self.font_name = "Roboto-Regular"  
        self.font_size = '20sp'
   

class CurrencyConverterScreen(Screen):

    CURRENCY_COUNTRY_MAP = {
        'USD': 'United States',
        'EUR': 'European Union',
        'GBP': 'United Kingdom',
        'JPY': 'Japan',
        'CAD': 'Canada',
        'AUD': 'Australia',
        'CNY': 'China',
        'INR': 'India',
        'NZD': 'New Zealand',
        'BRL': 'Brazil',
        'ZAR': 'South Africa',
        'PLN': 'Poland',
        'AFN': 'Afghanistan',
        'BDT': 'Bangladesh',
        'BYN': 'Belarus',
        'BGN': 'Bulgaria',
        'COP': 'Colombia',
        'CZK': 'Czech Republic',
        'DOP': 'Dominican Republic',
        'EGP': 'Egypt',
        'HKD': 'Hong-Kong',
        'HUF': 'Hungary',
        'ISK': 'Iceland',
        'IDR': 'Indonesia',
        'IRR': 'Iran',
        'ILS': 'Israel',
        'JMD': 'Jamaica',
        'KZT': 'Kazahstan',
        'KRW': 'Korea',
        'KES': 'Kenya',
        'LRD': 'Liberia',
        'LBP': 'Lebanon',
        'MGA': 'Madagascar',
        'MYR': 'Malaysia',
        'MVR': 'Maldives',
        'MXN': 'Mexico',
        'MAD': 'Morocco',
        'NDK': 'Norway',
        'PHP': 'Philippines',
        'RON': 'Romania',
        'RUB': 'Russia',
        'SGD': 'Singapore',
        'SEK': 'Sweden',
        'CHF': 'Switzerland',
        'THB': 'Thailand',
        'TRY': 'Turkey',
        'TND': 'Tunisia',
        'UAH': 'Ukraine',
        'AED': 'United Arab Emirates'
    }
    
    def __init__(self, **kwargs):
        super(CurrencyConverterScreen, self).__init__(**kwargs)
        self.name = 'converter_screen'
        self.layout = GridLayout(cols=2)

        with self.layout.canvas.before:
            Color(0.9, 1, 1)  
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)

        self.layout.bind(size=self._update_rect, pos=self._update_rect)

        # Fetch all available currencies from the API
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        self.currencies = [f'{code} ({self.CURRENCY_COUNTRY_MAP.get(code)})' 
                           for code in data['rates'].keys() if code in self.CURRENCY_COUNTRY_MAP.keys()]

        # Add widgets
        self.from_currency = CustomSpinner(
            text=self.currencies[0],
            values=self.currencies,
            size_hint=(.5, .2))
        self.layout.add_widget(self.from_currency)

        self.to_currency = CustomSpinner(
            text=self.currencies[1],
            values=self.currencies,
            size_hint=(.5, .2))
        self.layout.add_widget(self.to_currency)

        self.amount = TextInput(hint_text="Enter amount", multiline=False, size_hint=(1, .5), 
                        background_color=(240, 248, 255), font_name='Roboto', font_size='24sp')
        self.layout.add_widget(self.amount)

        self.result = Label(text='', color=(0, 0, 0, 1), size_hint=(1, .2), font_size='20sp', font_name="Roboto")
        self.layout.add_widget(self.result)

        convert_button = Button(text='Convert', size_hint=(1, .2), background_color=(0.5, 0.6, 0.9), font_size='20sp', font_name="Roboto")
        convert_button.bind(on_release=self.convert)
        self.layout.add_widget(convert_button)

        self.add_widget(self.layout)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def convert(self, instance):

        anim = (Animation(size_hint=(1, .2), background_color=(0.3, 0.4, 0.7, 1), duration=0.1) +
                Animation(size_hint=(1, .2), background_color=(0.5,0.6,0.9, 1), duration=0.3))
        
        # Start the animation
        anim.start(instance)
        print("Convert function called.")  # Debug statement
        try:
            amount = float(self.amount.text)
            print(f"Amount: {amount}")  # Debug statement
            from_currency = self.from_currency.text[:3]
            to_currency = self.to_currency.text[:3]

            response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
            response.raise_for_status()  # Raises a HTTPError if the response status is 4xx, 5xx
            data = response.json()

            rate = data['rates'][to_currency]
            print(f"Rate: {rate}")  # Debug statement
            converted_amount = amount * rate

            result_text = f"{amount} {from_currency} is equivalent to {converted_amount} {to_currency}"
            print(f"Result Text: {result_text}")  # Debug statement
            self.result.text = result_text

        except ValueError:
            self.result.text = "Error: Invalid input format. Please enter a number."
        except requests.exceptions.HTTPError as errh:
            self.result.text = f"Http Error: {errh}"
        except requests.exceptions.ConnectionError as errc:
            self.result.text = f"Error Connecting: {errc}"
        except requests.exceptions.Timeout as errt:
            self.result.text = f"Timeout Error: {errt}"
        except requests.exceptions.RequestException as err:
            self.result.text = f"Error: {err}"
class CurrencyConverterApp(App):
    def build(self):
        # Create a screen manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(CurrencyConverterScreen(name='converter_screen'))

        return screen_manager


if __name__ == "__main__":
    CurrencyConverterApp().run()

