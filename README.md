# nelder-mead-method
Nelder-Mead Optimalization Algorithm

----------------------------------------------------
Opis słowny
----------------------------------------------------

1.Losujemy trzy punkty z przestrzeni zmiennych decyzyjnych, dokonaj ich sortowania na podstawie wartości funkcji celu w danych punktach (np. malejąco). Ilość punktów zależna od ilości zmiennych decyzyjnych (n+1).

2.Uzyskaj nowy punkt poprzez ODBICIE (REFLECT) najgorszego punktu względem centroidu stworzonego z pozostałych punktów (w przypadku trzech punktów - odcinka).

a) Jeżeli nowy uzyskany punkt jest lepszy od DRUGIEGO najlepszego tworzącego odcinek,ale nie jest lepszy od najlepszego - zastąp najgorszy najlepszym punktem. Sprawdź warunki stopu.

b) Jeżeli nowy punkt jest lepszy od pozostałych (nowy najlepszy) to ROZSZERZ (EXPAND) czyli przesuń nowy punkt jeszcze dalej. Sprawdź czy nowy punkt po rozszerzeniu jest lepszy od punktu po odbiciu: tak - zastąp punktem po rozszerzeniu, nie - zastąp punktem po odbiciu. Sprawdź warunki stopu

3.Jeżeli ODBICIE oraz ROZSZERZENIE nie dało lepszego punktu to zastosuj SKURCZENIE (CONTRACT) dla najgorszego punktu.
Podziel odcinek znajdujący się pomiędzy punktem najgorszym, a odbitym na cztery części w taki sposób, aby punkt c1 znajdował się w 1/4 odcinka oraz c2 znajdował się w 3/4 odcinka. 
Oceń punkty c1 i c2. 
Jeśli któryś z punktów c1 i c2 są lepsze od drugiego najlepszego, zastąp najgorszy punkt najlepszym z c1 i c2. Sprawdź warunki stopu.

4.Jeżeli SKURCZENIE nie dało lepszego punktu to zastosuj ZMNIEJSZENIE (SHRINK). Przesuń najgorsze punkty w stronę najlepszego, o połowę odległości pomiędzy danym punktem, a najlepszym punktem. Sprawdź warunki stopu
