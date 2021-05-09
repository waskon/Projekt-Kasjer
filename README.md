9. Symulator kasjera Opis zadania
-	Okno podzielono jag na dwie części:
	Lewa: pusta. pojawiam się tam towary do skasowania
	prawa: przyciski od O do 9, przycisk 'backspace".Przycisk "Wyczyść" przycisk 'Zważ' oraz pole tekstowo - wciskanie przycisków cyfr powoduje dopisywanie ich do pola. backspace wymazuje ostawo wcisaną cyfrę. przycisk 'Wyczyść' czyści pale tekstowe.
Jeśli zawartość pola tekstowego to 1 i wciśnięty został przycisk cyfry. pole tekstowe jest czyszczone i dopisywana jest tam wybrana cyfra.
-	Na początku po lewej stronie znajduje się przypsk 'Następny klient', wciśnięcie go rozpoczyna grę (zapisanie aktualnego czasu i wyzerowanie kanele towarów)
-	W losowym miejscu lewe) strony okna pojawie się przycisk z:
	nazwo towaru i jogo IczebnoScią. np. 'Arbuz x10". Wciśnięcie przycisku powoduje zmniejszenie liczebności towaru o tyle. de wpisane jest w palu tekstowym po prawej stronie. a pole lo jest czyszczone (zawartość ustawiana na 1) lub
	nazwą towaru r napisem lkit oznaczającym. że jest to towar do zwalenia. Jego kasowanie polega na kliknięciu Przycisku z towarem. następnie klemiędu przycisku -Zwat'. a następie ponownym kliknięciu przycisku z towarem. Po naciśnięciu przycisku 'Zważ' etykieta towaru powinna się zmienić (rre byt podana losowa waga od 0.05 do 2 kg).
- Jeśli wartość pola tekstowego po prawej stronie przewyższa liczebność towaru. to gracz przegrywa I wyświetlane jest okno Informujące o tym.
-	Po skasowaniu towaru (liczebność spadki do 0). do licznika towarów dodawana jest oryginalna liczebność towaru. oraz generowany jest kolejny towar.
-	Generowane jest od 10 do 20 towarów, polowa z nich na sztuki. Liczba sztuk ma wynosić od 1 do 50 (losowo). Prawdopodobienstwo wylosowania liczebności ł (pojedynczy artykul) ma wynosić 50%.
-	Po skasowaniu wszystkich towarów wy
świetlany jest średni czas kasowania 
jednego przedmiotu (towar w Iczobności 10 liczy Się za 10 przedmiotCw).
-	Nazwy towarów mają być lasowane z minimum dwudziestoelementowej listy.
-	Towary mają byt reprezentowane przez obiekty TowarNaSztuki i
TOvrarNaWagę dziedziczących po klasie TOwar. W obiektach ma być
przechowywana nazwa towaru. liczba sztuk lub wago czas pcSwienia się w lewej części okna I czas skasowania.
Testy
1.	Skasowanie towaru na sztuki po klikając na niego kilka razy.
2.	Skasowanie towary na sztuki wpisując jego liczność i klikając raz. Wymagane jest resetowanie pola do wartości 1.
3.	Próba skasowania towaru na sztuki wpisując zbyt dużą liczność
(OCzeknvana intomiacja O przcgMnej).
4.	Próba zważenia towaru na sztuki (oczekiwana informacga o przegnanej).
17
17
5.	Próba skasowania towaru na wagę jakby byt towarem na szoki
(oczekiwana informacja o przegranej).
6.	Skasowanie wszystkich towarów (oczekiwane okno z podsumowaniem symulacji).
7.	Pokazanie. to fozebnott 1 występuje cdpoweelnkt często.
