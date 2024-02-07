# Zaliczenie_Proj_app_rozp
Maciej 157116


Zadanie 1

REST API: ipify

URL: https://api.ipify.org/?format=json

Metoda: GET - Zwraca publiczny adres IP klienta w formacie JSON.

#########

SOAP API: CountryInfoService

URL: http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso

WSDL: http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL

Metody:
ListOfCountryNamesByName - Zwraca listę nazw krajów, posortowaną alfabetycznie.
CountryFlag - Zwraca URL do obrazka flagi danego kraju.

########

wymagane biblioteki:
Python: requests dla REST API, zeep dla SOAP API.

###################################
Zadanie 2

Wybrałem moduł TCP ponieważ zapewnienia niezawodną komunikację pomiędzy klientem a serwerem,
umożliwiając strumieniową wymianę danych z potwierdzeniem odbioru.


Prosty protokół komunikacyjny opierający się na komunikatach tekstowych z predefiniowanymi
komendami i odpowiedziami wykorzystując przykłady z zadania 1


Komendy Klienta:
GET_IP - żądanie przesłania lokalnego adresu IP klienta.
GET_COUNTRIES - żądanie przesłania listy nazw krajów.
Odpowiedzi Serwera:
Dla GET_IP: Odpowiedź to string zawierający lokalny adres IP klienta.
Dla GET_COUNTRIES: Odpowiedź to lista nazw krajów, każda nazwa w nowej linii.

Zadania Serwera:
-Nasłuchiwanie na określonym porcie TCP (w naszym przypadku 9999)
-identyfikacja żądania klienta (GET_IP lub GET_COUNTRIES)
-Generowanie i wysyłanie wiadomości zwrotnej zgodnej z żądaniem Clienta

Zadania Clienta:
-Nawiązywanie połączenia z Serwerem (za pośrednictwem portu 9999)
-Wysyłanie żądań do serwera.
-Odbieranie i wyświetlanie otrzymanych odpowiedzi od Serwera


Wynik działania:

Wyświetlenie w konsoli odpowiedzi na zapytania: GET_IP i GET_COUNTRY w zależności
które zostało przesłane (na potrzeby testu wysyłamy oba zapytania)

Odpowiedź na GET_IP otrzymujemy formułe:
"Otrzymana odpowiedź:  twój local ip to 192.168.0.5"

Odpowieź na GET_COUNTRY otrzymujemy formułe:
"Otrzymana odpowiedź:
Polska
Niemcy
Francja"
