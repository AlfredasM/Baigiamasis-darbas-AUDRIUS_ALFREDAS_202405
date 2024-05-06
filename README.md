Baigiamasis darbas 2024-05


Baigiamasis darbas (Duomenų mokslas)

Darba atliko : Audrius Janikūnas ir Alfredas Motuzas

Darbo tikslas : Išanalizuoti elektroninės dviračių parduotuvės vienų metų pardavimo duomenis ir pateikti išvadas,
                bei prognozes.

Darbo eiga :

Parduotuvės realus elektroninis adresas : ( https://www.99bikes.com.au/ )

    - duomenų rinkinio analizė ir apžvalga naudojant 'PANDAS' :
        * duomenų rinkinio apžvalga
![img_1.png](img_1.png)

        * visu pardavimu skaičius ir vidutinė kaina pagal dviračių tipą (Kalnų, plentinis, hibridas, turistinis)
![img_10.png](img_10.png)

        * pardavimų skaičius pagal mėnesius (grafikas)
![img_32.png](img_32.png)

        * pardavimu skaičius pagal dviračiu tipus (grafinis atvaizdavimas)
![img_33.png](img_33.png)

        
        * pardavimus skaičius pagal dviračiu klases (grafinis atvaizdavimas)
![img_40.png](img_40.png)
        
        * sujungiame tris skirtingus 'excel sheet' (pardavimų ir klientų duomenų pagal 'kliento_id' ir gyvenamąją vietą
            pagal 'kliento_id'), kad galėtume analizuoti duomenis su daugiau parametrų.

![img_17.png](img_17.png)
     
       
        * pirkimų skaičius pagal lytį skaiciavimas
![img_9.png](img_9.png)


        * pirkimu skaičius pagal lytį ir pagal apskritis grafikas
![img_35.png](img_35.png)

        * apskričių žemėlapis
![img_8.png](img_8.png)

        * demografija:

![img_44.png](img_44.png)


     - duomenų rinkinio analizė naudojant mašininio mokymo metodus:

        * Kmeans metodas
![img_36.png](img_36.png)

        * DBscan metodas taip pat paskaičiuojamas geriausias clusters kiekis pagal Elbow (su keliais bandymais
            gaunamas 2-3 optimalus cl. skaičius)
![img_47.png](img_47.png)

    *DBSCAN metodui Elbow grafikas
![img_48.png](img_48.png)

        * RandomForest metodas
![img_31.png](img_31.png)

        * AgglomerativeClustering metodas
![img_45.png](img_45.png)

        * LinearRegression metodas
![img_39.png](img_39.png)

    - MSE, RMSE, R2 (metrikos - 'Mean squared error', 'Root Mean Squared Error', 'R-squared )
![img_21.png](img_21.png)
        
        - ROC (ROC kreive pagal ONLINE ir fizinius pirkimus)
![img_15.png](img_15.png)

![img_16.png](img_16.png)

        * Dviračių kainų palyginimas 2017 metų ir 2024 metų (naudojant 'Scraping' realių kainų surinkimui)

    -Grafinis atvaizdavimas 2017 metų ir 2024 metų

![img_6.png](img_6.png)

    -Skaičiavimas

![img_30.png](img_30.png)



     - duomenų rinkinio analizė naudojant neuroninius tinklus:

        * KerasClassifier
![img_41.png](img_41.png)
    
    Model accuracy: 0.7999
    
    - Modelio tikslumas
![img_42.png](img_42.png)

    - Modelio nuostoliai

![img_43.png](img_43.png)




        


    Išvados, komentarai/pasiūlymai, sunkumai su kuriais teko susidurti:

    Išvados:
    
    - Parduotuvės metinė apyvarta - 22 MLN. EUR

    - Kas mėnesį parduodamos produkcijos ~ 2 MLN. EUR

    - Birželį ir rugsėjį pastebimi nežymus pardavimu kritimai (galima butų tais mėnesiais, didinti reklamos apimtis,
        arba taikyti akcijas, kad padidinti pardavimus).

    - Iš grafikų matome, kad didžiausia marža vidutinės klasės dviračių.

    - Vyrų ir moterų dviračiu pirkimas praktiškai 50%/50%.

    - Pasiskirstymas pagal regioną labai akivaizdus, daugiausia nuperkama dviračių kur gyventojų tankumas
        yra didžiausias (Sidnėjus - didžiausias Australijos miestas), o ne didžiausias  teritorijos plotas. 
        (galima būtų plėsti pardavimus į SouthAustralia regioną, logistiškai tinkamoje, taip pat didinti
        reklama Victoria regione ir Queensland regione)

    - Pirkimo pasiskirstymas pagal pirkėjų amžių : matome aiškiai 3 išskirtas grupes, ir kad jaunesni
        žmonės labiau perka brangesnius dviračius.
    
    - Didžiausią įtaką kainai daro : 
                            1- Gamintojas ('brand'),
                            2- Pirkėjo gimimo metai,
                            3- Dviračio dydis,
                            4- Dviračio klasė.

    - Pagal aksesuarų ir dalių pirkimą jaunesni žmonės šiek tiek daugiau atliko pirkimu per 3 metus po
        dviračio pirkimo. (galima pagal metus siūlyti papildomas akcijas aksesuarų ir dalių,
        siuntinėti reklamą)

    - Iš ROC kreives matome kad pagal pirkimus 'ONLINE' ir fizinius  modelio tikslumas artimas 'aklam'
        spėliojimui, ir iš pateiktų (apskaičiuotų) duomenų matome, kad modelis negalėjo apsimokyti, nes
        pirkimai yra ~ 50%/50%.

    - Palyginus Scraping duomenis dviračių tipų 2024m. ir 2017m 'dataset' matome, kad dviračiai stipriai
        pabrango, per 7 metus, bet reikalinga detalesne analizė, nes atsirado labai daug elektrinių
        dviračių, kas labai stipriai įtakoja kainą. Parinkome dviračių tipą kuriame mažiausiai elektrinių
        dviračių segmente, ir 2017 m. 2024 m. kainų kilimas tiksliausias. (Matoma, kad vienodo tipo
        dviračių kainų kilimas rinkoje ~ 10%)
    
    Komentarai / pasiūlymai:

    - Darbo metu labai svarbu planuotis laika, nes vien duomenų valymui galima sugaišti visą savaitę
        (siekiant idealumo), turint ribotą laiką galima tvarkytis tik tuos duomenis su kuriais dirbama.
        
    Sunkumai:
    - Su neuroniniais tinklais dar reikėtų pagilinti žinias, sugaišome daugiausia laiko, bet rezultatais  nesame labai
        patenkinti.

        TIKRAI YRA KUR TOBULĖTI...

![img_51.png](img_51.png)

    AČIŪ UŽ DĖMESĮ...



    
    
    

