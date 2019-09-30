Słonie
Limit pamięci: 64 MB

W Bajtockim Zoo ma się za chwilę odbyć parada, w której uczestniczyć będą wszystkie znajdujące się w nim słonie. Pracownicy zoo zachęcili już zwierzęta do ustawienia się w jednym rzędzie, gdyż zgodnie z zarządzeniem dyrektora zoo taka powinna być początkowa figura parady.

Niestety, na miejsce przybył sam dyrektor i zupełnie nie spodobała mu się wybrana przez pracowników kolejność słoni. Dyrektor zaproponował kolejność, w której według niego zwierzęta będą się najlepiej prezentować, i wydał pracownikom polecenie poprzestawiania słoni zgodnie z tą propozycją.

Aby uniknąć nadmiernego chaosu tuż przed paradą, pracownicy postanowili przestawiać słonie, zamieniając miejscami kolejno pewne pary słoni. Przestawiane zwierzęta nie muszą sąsiadować ze sobą w rzędzie. Wysiłek potrzebny do nakłonienia słonia do ruszenia się z miejsca jest wprost proporcjonalny do jego masy, a zatem wysiłek związany z zamianą miejscami dwóch słoni o masach  oraz  można oszacować przez . Jakim minimalnym wysiłkiem pracownicy mogą poprzestawiać słonie tak, aby usatysfakcjonować dyrektora?

Napisz program, który:

wczyta ze standardowego wejścia masy wszystkich słoni z zoo oraz aktualną i docelową kolejność słoni w rzędzie,
wyznaczy taki sposób poprzestawiania słoni, który prowadzi od kolejności początkowej do docelowej i minimalizuje sumę wysiłków związanych ze wszystkimi wykonanymi zamianami pozycji słoni,
wypisze sumę wartości tych wysiłków na standardowe wyjście.
Wejście
Pierwszy wiersz wejścia zawiera jedną liczbę całkowitą  (), oznaczającą liczbę słoni w Bajtockim Zoo. Dla uproszczenia zakładamy, że słonie są ponumerowane od  do . Drugi wiersz zawiera  liczb całkowitych  ( dla ), pooddzielanych pojedynczymi odstępami i oznaczających masy poszczególnych słoni (wyrażone w kilogramach).

Trzeci wiersz wejścia zawiera  różnych liczb całkowitych  (), pooddzielanych pojedynczymi odstępami i oznaczających numery kolejnych słoni w aktualnym ustawieniu. Czwarty wiersz zawiera  różnych liczb całkowitych  (), pooddzielanych pojedynczymi odstępami i oznaczających numery kolejnych słoni w ustawieniu proponowanym przez dyrektora zoo. Możesz założyć, że ustawienia reprezentowane przez ciągi  oraz  są różne.

Wyjście
Pierwszy i jedyny wiersz wyjścia powinien zawierać jedną liczbę całkowitą, oznaczającą minimalny łączny wysiłek związany z poprzestawianiem słoni, w wyniku którego z ustawienia reprezentowanego przez  uzyskuje się ustawienie .

Przykład
Dla danych wejściowych:

6
2400 2000 1200 2400 1600 4000
1 4 5 3 6 2
5 3 2 4 6 1
poprawną odpowiedzią jest:

11200
Jeden z najlepszych sposobów poprzestawiania słoni uzyskujemy, zamieniając miejscami kolejno pary słoni:

2 i 5 - wysiłek związany z zamianą to , a uzyskane ustawienie to 1 4 2 3 6 5,
3 i 4 - wysiłek to , a uzyskane ustawienie to 1 3 2 4 6 5,
1 i 5 - wysiłek to , a uzyskane ustawienie to 5 3 2 4 6 1, czyli ustawienie docelowe.
Autorzy zadania: Jakub Radoszewski, Wojciech Rytter.
